<div align="center"><img src="assets/domainsentry.svg" alt="DomainSentry Logo" width="200" height="200"></div>

<div align="center"> # DomainSentry - The Ultimate WHOIS Extractor </div>

[![PyPI version](https://badge.fury.io/py/domainsentry.svg)](https://badge.fury.io/py/domainsentry)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/domainsentry.svg)](https://pypi.org/project/domainsentry/)
[![Build Status](https://travis-ci.org/thebitdoodler/domainsentry.svg?branch=main)](https://travis-ci.org/thebitdoodler/domainsentry)
[![Coverage Status](https://coveralls.io/repos/github/thebitdoodler/domainsentry/badge.svg?branch=main)](https://coveralls.io/github/thebitdoodler/domainsentry?branch=main)
[![Docker Pulls](https://img.shields.io/docker/pulls/thebitdoodler/domainsentry.svg)](https://hub.docker.com/r/thebitdoodler/domainsentry/)

DomainSentry is a powerful and flexible tool designed to perform WHOIS lookups on a list of domains or URLs. It supports both a command-line interface (CLI) for system-level operation and a web-based interface using Streamlit, which can be easily deployed using Docker.

## 🚀 Features

- 🔍 Extract domains from URLs
- 📊 Perform bulk WHOIS lookups
- 📁 Output results to terminal or CSV
- 🖥️ CLI for system-level operation
- 🐳 Docker support for easy deployment of the web interface
- 🌐 Web interface using Streamlit

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
  - [Streamlit Web Interface](#streamlit-web-interface)
- [Development](#development)
- [Contributing](#Contributing)
- [License](#License)

## 🔧 Installation

### Using pip (for CLI)

```bash
pip install domainsentry
```

### Using Docker (for Streamlit web interface)

```bash
docker pull thebitdoodler/domainsentry
```

## 🖥️ Usage

### CLI Usage

The CLI version runs directly on your system:

```bash
# Output to terminal
domainsentry input_file.txt

# Output to CSV
domainsentry input_file.txt -o csv -f output.csv
```

### Streamlit Web Interface

#### Running Locally

If you want to run the Streamlit interface locally without Docker:

```bash
streamlit run domainsentry/streamlit_app.py
```

#### Using Docker

To run the Streamlit interface using Docker:

```bash
docker run -p 8501:8501 thebitdoodler/domainsentry
```

Then open your web browser and navigate to `http://localhost:8501`.

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/thebitdoodler/domainsentry.git
   cd domainsentry
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   pytest tests/
   ```

## Contributing

We welcome contributions to DomainSentry! Please see our [Contributing Guide](CONTRIBUTING.md) for more details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [python-whois](https://github.com/richardpenman/whois) for WHOIS lookup functionality
- [Streamlit](https://streamlit.io/) for the web interface

## 📞 Contact

For questions and support, please open an issue on the GitHub repository.