# 🧪 QA Test Automation Suite

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

An automated end-to-end (E2E) and HTTP health verification suite built with `pytest`, Playwright, Docker, and GitHub Actions for continuous UI and endpoint smoke testing.

---

# 📝 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Usage](#-installation--usage)
- [Project Structure](#-project-structure)
- [License](#-license)

---

# 📌 About the Project

**QA Test Automation Suite** provides a containerized, CI-ready quality assurance framework combining fast HTTP health checks with headless Chromium browser smoke tests via `pytest-playwright`. Every run generates a self-contained HTML test report (`reports/report.html`) and archives it as a downloadable GitHub Actions workflow artifact on every push and pull request to `main`.

---

# ✨ Features

- ✅ **HTTP Health & Endpoint Verification** — Automated status code and response checks for target web endpoints.
- ✅ **UI Smoke & E2E Browser Tests (`Playwright`)** — Headless Chromium assertions verifying page rendering, DOM elements, and core user flows against live targets (including `https://halukcansarioz.github.io/`).
- ✅ **Self-Contained HTML Reporting (`pytest-html`)** — Generates portable, detailed test execution reports in `reports/report.html`.
- ✅ **Dockerized Execution** — Reproducible test environment based on Microsoft's official `mcr.microsoft.com/playwright/python` image.
- ✅ **Automated CI Pipeline** — Runs on every `push` and `pull_request` to `main` via `.github/workflows/ci.yml`, uploading `reports/report.html` as a workflow artifact.

---

# 🛠 Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Test Framework** | pytest | Modular test discovery, fixtures, and assertions |
| **Browser Automation** | Playwright (`pytest-playwright`) | Headless Chromium UI smoke & E2E testing |
| **Reporting** | `pytest-html` | Self-contained HTML execution reports |
| **Language** | Python 3.11 | Core test scripting runtime |
| **Containerization** | Docker | Isolated, dependency-free test execution |
| **CI/CD** | GitHub Actions | Automated test runs & artifact archiving |

---

# ⚙️ Installation & Usage

### 1. Local Setup

```bash
git clone git@github.com:halukcansarioz/qa-test-automation-suite.git
cd qa-test-automation-suite
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

### 2. Running Tests Locally

```bash
pytest -v --html=reports/report.html --self-contained-html
```

### 3. Running with Docker

```bash
docker build -t qa-test-automation-suite .
docker run --rm -v $(pwd)/reports:/app/reports qa-test-automation-suite
```

The generated report will be available at `reports/report.html`.

---

# 📁 Project Structure

```text
qa-test-automation-suite/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI & report artifact upload
├── tests/                  # HTTP health & Playwright UI smoke tests
├── Dockerfile              # Playwright Python container image
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── requirements.txt        # Python & Playwright dependencies
```

---

# 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
