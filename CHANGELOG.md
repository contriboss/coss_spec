# Changelog

All notable changes to the COSS specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.0.3 (2025-07-14)


### Features

* add Package URL (PURL) support and fix COSS naming ([ecf53b3](https://github.com/contriboss/coss_spec/commit/ecf53b3d2fd5f6d28a320563189e00e0deef7ab3))
* add Package URL (PURL) support for vendor-agnostic package identification ([fec5059](https://github.com/contriboss/coss_spec/commit/fec50593e558ed36d2c31d0696aadb60153e08fe))


### Bug Fixes

* configure release-please for simple release type ([dd0a0ec](https://github.com/contriboss/coss_spec/commit/dd0a0ecbef2e035c8862d6b064963b115d474df3))
* handle TOML fields in packaging section during validation ([af619e6](https://github.com/contriboss/coss_spec/commit/af619e61c6c6bdde1ecf3c972a91c90675a58848))
* install instructions ([4ec3502](https://github.com/contriboss/coss_spec/commit/4ec3502ac59533e6dad2a214f83c453db51c99d3))

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
