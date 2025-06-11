# Changelog

All notable changes to the COSS specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2025-06-11

### Added
- **Submodules Support**: New `[submodules]` section for modular COSS architectures
- Support for referencing other COSS files via git URLs, HTTP URLs, and relative paths
- Extended format for custom paths and version specifications
- Enables multi-repo and microservice architecture support

### Examples
- `frontend = "git@github.com:company/frontend.git"`
- `backend = "https://raw.githubusercontent.com/company/backend/main/coss.toml"`
- `shared = "./shared/coss.toml"`
- `api = { source = "git@github.com:company/api.git", path = "coss.toml", version = "v1.2.0" }`

## [0.0.1] - 2025-06-10

### Added
- Initial release of COSS (Contriboss Open Source Standard) specification
- Comprehensive metadata template with 19 major sections
- Versioned specification structure in `versions/` directory
- README with curl installation instructions
- MIT License
- Basic project structure for specification repository

### Features
- **Required Fields**: Basic project info, repository, languages, build/test commands, maintainers
- **Optional Fields**: Dependencies, quality tooling, security, documentation, i18n
- **Version Management**: Symlinked latest version for easy access
- **Easy Installation**: One-line curl command for template download

[Unreleased]: https://github.com/contriboss/coss_spec/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/contriboss/coss_spec/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/contriboss/coss_spec/releases/tag/v0.0.1
