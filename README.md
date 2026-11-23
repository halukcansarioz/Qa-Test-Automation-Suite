# qa-test-automation-suite
[![CI](https://github.com/halukcansarioz/qa-test-automation-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/halukcansarioz/qa-test-automation-suite/actions/workflows/ci.yml)

Modular V&V and end-to-end test automation framework built with Python, pytest, Playwright, Docker, and GitHub Actions CI.

## Architecture

The framework is organized into modular components for maintainability, containerized execution, and automated CI/CD reporting:

```text
qa-test-automation-suite/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI workflow
├── tests/
│   └── test_portfolio_smoke.py     # Smoke & E2E tests for https://halukcansarioz.github.io/
├── Dockerfile                      # Containerized Playwright test runner
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
└── README.md                       # Project documentation
```

### Key Components
- **Test Runner (`pytest` + `pytest-playwright`)**: Executes HTTP status checks and browser-based E2E assertions against `https://halukcansarioz.github.io/`.
- **HTML Reporting (`pytest-html`)**: Generates self-contained HTML execution reports at `reports/report.html`.
- **Containerization (`Dockerfile`)**: Uses `mcr.microsoft.com/playwright/python:latest` with pre-configured browser dependencies for reproducible runs.
- **CI Pipeline (`.github/workflows/ci.yml`)**: Automates test execution and artifact archiving on every `push` and `pull_request` to `main`.

## Setup

### Prerequisites
- Python 3.11+
- `pip`

### Local Installation

1. Clone the repository and enter the project directory:
   ```bash
   git clone <repository-url>
   cd qa-test-automation-suite
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies and Playwright Chromium:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. Run the test suite:
   ```bash
   pytest -v --html=reports/report.html --self-contained-html
   ```

## Running with Docker

Build and run the test suite inside a Docker container without installing Python or browsers locally:

1. Build the Docker image:
   ```bash
   docker build -t qa-test-automation-suite .
   ```

2. Run the container and mount the `reports` directory to access the generated HTML report on the host:
   ```bash
   docker run --rm -v $(pwd)/reports:/app/reports qa-test-automation-suite
   ```

## CI/CD & Reporting

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs automatically on `push` and `pull_request` events targeting the `main` branch:

1. **Environment Setup**: Provisions Ubuntu with Python 3.11.
2. **Dependency Installation**: Installs packages from `requirements.txt` and downloads Playwright Chromium with system dependencies.
3. **Test Execution**: Runs `pytest -v --html=reports/report.html --self-contained-html`.
4. **Artifact Upload**: Uploads `reports/report.html` as a workflow artifact, downloadable directly from the GitHub Actions run summary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. Playwright, Docker, and GitHub Actions CI.
