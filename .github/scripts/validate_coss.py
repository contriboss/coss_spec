#!/usr/bin/env python3
"""Validate COSS specification files."""

import os
import re
import sys
import tomllib
from pathlib import Path


def find_toml_files(directory="."):
    """Find all TOML files in the directory tree."""
    toml_files = []
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.toml'):
                toml_files.append(Path(root) / file)
    
    return toml_files


def validate_toml_syntax(file_path):
    """Validate TOML file syntax."""
    try:
        with open(file_path, 'rb') as f:
            tomllib.load(f)
        return True, None
    except Exception as e:
        return False, str(e)


def validate_coss_structure(file_path):
    """Validate COSS specification structure."""
    required_fields = [
        'name', 'version', 'description', 'licenses', 
        'ai_contributions', 'coss_compliant', 'repository', 
        'languages', 'maintainers', 'governance', 'build', 'test'
    ]
    
    try:
        with open(file_path, 'rb') as f:
            data = tomllib.load(f)
        
        is_template = data.get('name', '') == ''
        
        # Check for fields at top level or in packaging section (due to template structure issue)
        def field_exists(field_name):
            return field_name in data or (
                'packaging' in data and field_name in data['packaging']
            )
        
        def get_field_value(field_name):
            if field_name in data:
                return data[field_name]
            elif 'packaging' in data and field_name in data['packaging']:
                return data['packaging'][field_name]
            return None
        
        if is_template:
            # For templates, just check field existence
            missing_fields = [field for field in required_fields if not field_exists(field)]
            if missing_fields:
                return False, f"Missing required fields: {', '.join(missing_fields)}"
        else:
            # For filled files, check that required fields are not empty
            empty_fields = []
            for field in required_fields:
                value = get_field_value(field)
                if value is None or value == '' or \
                   (isinstance(value, list) and len(value) == 0) or \
                   (isinstance(value, dict) and len(value) == 0):
                    empty_fields.append(field)
            
            if empty_fields:
                return False, f"Empty required fields: {', '.join(empty_fields)}"
        
        return True, None
    except Exception as e:
        return False, f"Error parsing file: {str(e)}"


def check_version_consistency():
    """Check version consistency across files."""
    main_toml_path = Path('coss.toml')
    
    if not main_toml_path.exists():
        return False, "Main coss.toml file not found"
    
    # Extract version from header comment
    with open(main_toml_path, 'r') as f:
        content = f.read()
    
    version_match = re.search(r'# COSS Metadata Template v(\d+\.\d+\.\d+)', content)
    
    if not version_match:
        return False, "Could not find version in main coss.toml header"
    
    main_version = version_match.group(1)
    print(f"📌 Main template version: v{main_version}")
    
    # Check version directory exists
    version_dir = Path(f'versions/v{main_version}')
    if not version_dir.exists():
        return False, f"Version directory {version_dir} does not exist"
    
    # Check symlink
    if main_toml_path.is_symlink():
        link_target = os.readlink(main_toml_path)
        expected_target = f'versions/v{main_version}/coss.toml'
        
        if link_target != expected_target:
            return False, f"Symlink points to {link_target}, expected {expected_target}"
    else:
        print("⚠️  coss.toml is not a symlink")
    
    return True, None


def main():
    """Main validation function."""
    has_errors = False
    
    # 1. Validate TOML syntax
    print("🔍 Validating TOML syntax...")
    toml_files = find_toml_files()
    
    for file_path in toml_files:
        is_valid, error = validate_toml_syntax(file_path)
        if is_valid:
            print(f"✅ {file_path} - Valid TOML syntax")
        else:
            print(f"❌ {file_path} - Invalid TOML: {error}")
            has_errors = True
    
    # 2. Validate COSS specification structure
    print("\n📋 Validating COSS specification structure...")
    for file_path in toml_files:
        if file_path.name == 'coss.toml':
            is_valid, error = validate_coss_structure(file_path)
            if is_valid:
                print(f"✅ {file_path} - Structure validation passed")
            else:
                print(f"❌ {file_path} - {error}")
                has_errors = True
    
    # 3. Check version consistency
    print("\n🔢 Checking version consistency...")
    is_valid, error = check_version_consistency()
    if is_valid:
        print("✅ Version consistency check passed")
    else:
        print(f"❌ {error}")
        has_errors = True
    
    # Summary
    if has_errors:
        print("\n❌ Validation failed! Please fix the errors above.")
        sys.exit(1)
    else:
        print("\n✅ All validations passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()