#!/bin/bash
set -e

# COSS Specification Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/install.sh | sh

LATEST_VERSION="v0.0.2"
REPO_URL="https://raw.githubusercontent.com/contriboss/coss_spec/master"

echo "🔧 Installing COSS specification..."

# Check if coss.toml already exists
if [ -f "coss.toml" ]; then
    echo "⚠️  coss.toml already exists. Creating backup as coss.toml.backup"
    cp coss.toml coss.toml.backup
fi

# Download the latest version
echo "📥 Downloading COSS specification $LATEST_VERSION..."
curl -fsSL "$REPO_URL/versions/$LATEST_VERSION/coss.toml" -o coss.toml

if [ -f "coss.toml" ]; then
    echo "✅ COSS specification installed successfully!"
    echo ""
    echo "📝 Next steps:"
    echo "1. Edit coss.toml with your project information"
    echo "2. Fill in the required fields (name, version, description, etc.)"
    echo "3. Remove or customize optional sections as needed"
    echo ""
    echo "📚 Documentation: https://contriboss.com/standard"
    echo "🆘 Help: https://github.com/contriboss/coss_spec/issues"
else
    echo "❌ Installation failed. Please try again or report an issue."
    exit 1
fi