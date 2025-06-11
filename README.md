# COSS Specification

The official specification repository for COSS (Contriboss Open Source Standard) - promoting software neutrality and anti-vendor lock-in principles.

## Quick Installation

Install the latest COSS specification template to your project:

```bash
curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/install.sh | sh
```

Or download directly:

```bash
curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/versions/v0.0.2/coss.toml -o coss.toml
```

## What is COSS?

COSS (Contriboss Open Source Standard) is a comprehensive metadata specification that promotes:

- **Software Neutrality**: Avoiding vendor lock-in through standardized metadata
- **Project Transparency**: Clear documentation of dependencies, governance, and practices
- **Community Trust**: Standardized information for informed decision-making
- **Development Best Practices**: Encouraging quality, security, and maintainability

## Usage

1. **Download the template** using the curl command above
2. **Customize the coss.toml file** with your project's information
3. **Commit the file** to your repository root
4. **Keep it updated** as your project evolves

## Specification Structure

The COSS specification is organized into the following sections:

### Required Fields
- **Basic Project Information**: Name, version, description, licenses
- **Repository Information**: Repository URL, issue tracking
- **Languages and Frameworks**: Primary technologies used
- **Build and Test Commands**: How to build and test the project
- **Maintainers and Governance**: Who maintains the project and how

### Optional Fields
- **Dependency Management**: Lock files and packaging commands
- **Quality Tooling**: Linting, formatting, static analysis
- **Security and Compliance**: Vulnerability scanning, SBOM
- **Documentation**: Coverage metrics and style guides
- **Internationalization**: Locale and translation support
- **Community Features**: Chat, support channels, contribution tools

## Versioning

This repository follows semantic versioning. Each version of the specification is available in the `versions/` directory:

- `versions/v0.0.1/` - Initial specification (19 sections)
- `versions/v0.0.2/` - Added submodules support for modular architectures
- `coss.toml` - Symlink to the latest version (currently v0.0.2)

## Installation by Version

To download a specific version:

```bash
# Install latest with script (recommended)
curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/install.sh | sh

# Download specific versions directly
curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/versions/v0.0.1/coss.toml -o coss.toml
curl -fsSL https://raw.githubusercontent.com/contriboss/coss_spec/master/versions/v0.0.2/coss.toml -o coss.toml
```

### Version Features

- **v0.0.1**: Core COSS specification with 19 sections covering all essential metadata
- **v0.0.2**: Adds optional `[submodules]` section - works for single projects (leave empty) or multi-repo architectures

## Example Projects

See real-world examples of COSS-compliant projects:

- [Contriboss Website](https://github.com/contriboss/contriboss) - Static website using Astro
- [More examples coming soon...]

## Contributing

We welcome contributions to improve the COSS specification:

1. **Issues**: Report problems or suggest improvements
2. **Pull Requests**: Propose changes to the specification
3. **Discussion**: Join conversations about open source standards

## License

This specification is released under the MIT License. See [LICENSE](LICENSE) for details.

## Learn More

- **Website**: [contriboss.com](https://contriboss.com)
- **Documentation**: [contriboss.com/standard](https://contriboss.com/standard)
- **Community**: [contriboss.com/community](https://contriboss.com/community)

---

*COSS promotes software neutrality, transparency, and community trust in open source projects.*
