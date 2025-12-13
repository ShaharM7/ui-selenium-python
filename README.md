# UI Selenium Python — Automation Portfolio

## Project overview

This project contains UI automation tests written in Python using Selenium and pytest. Tests exercise the web UI through
browser automation (Chrome/Firefox). The test suite is organized to keep tests, page objects, fixtures, and helpers
separated so tests are readable and maintainable.

Typical flow:

- Tests invoke high-level steps.
- Page objects map pages/components to Selenium actions.
- Fixtures initialize the WebDriver and provide setup/teardown.
- Assertions check expected UI outcomes.

## Prerequisites

- Windows 10/11 (commands below assume Windows)
- Python 3.8+ installed and available on PATH
- Git (optional, for cloning)
- Chrome or Firefox installed (the browser you will run tests with)
- pip (bundled with Python)

Recommended (optional):

- Install `virtualenv` or use built-in venv module.

## Folder structure (example)

- tests/ — pytest test files
- pages/ — Page Object classes
- fixtures/ — pytest fixtures (driver setup, config)
- resources/ — test data, locators
- requirements.txt — pinned Python dependencies (if present)

## Setup — create virtual environment and install packages

Open a Windows command prompt (cmd) or PowerShell and run:

1) Clone or open repo and change directory

```
cd C:\Projects\portfolio\automation-portfolio\ui-selenium-python
```

2) Create a virtual environment (Windows)
   Command Prompt:

```
python -m venv venv
venv\Scripts\activate
```

PowerShell:

```
python -m venv venv
venv\Scripts\Activate.ps1
```

3) Upgrade pip (recommended)

```
python -m pip install --upgrade pip
```

4) Install packages

- If the repository includes a requirements.txt:

```
pip install -r requirements.txt
```

- If there is no requirements.txt, install common packages used here:

```
pip install selenium pytest webdriver-manager
```

(If you prefer Firefox: install `geckodriver` or `webdriver-manager` will handle drivers for you.)

## Browser driver options

Option A — webdriver-manager (recommended for simplicity)

- The `webdriver-manager` package automatically downloads matching browser drivers.
- Example usage inside fixtures:
    - from webdriver_manager.chrome import ChromeDriverManager
    - driver = webdriver.Chrome(ChromeDriverManager().install())

Option B — manually install driver

- Download ChromeDriver matching your Chrome version: https://chromedriver.chromium.org/downloads
- Put chromedriver.exe in a PATH directory or specify path when creating WebDriver:

```
driver = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
```

## Running tests

Prerequisites
- Python 3.8+ installed.
- From project root.

Quick setup (Windows)
1. Create & activate venv:
   py -3 -m venv venv
   venv\Scripts\activate
2. Install deps:
   pip install -r requirements.txt

Quick setup (macOS / Linux)
1. Create & activate venv:
   python3 -m venv venv
   source venv/bin/activate
2. Install deps:
   pip install -r requirements.txt

Run all tests
- From project root:
  pytest

Common options
- Run with more verbose output:
  pytest -q
- Run a single test file:
  pytest tests/test_example.py
- Run a single test case:
  pytest tests/test_example.py::test_name
- Generate an HTML report (requires pytest-html):
  pytest --html=reports/report.html --self-contained-html
- Run tests in parallel (requires pytest-xdist):
  pytest -n auto

Environment variables (examples)
- Select browser (default from config if unset):
  Windows:  set BROWSER=chrome
  macOS/Linux: export BROWSER=chrome
- Run in headless mode:
  Windows:  set HEADLESS=true
  macOS/Linux: export HEADLESS=true

Examples
- Run all tests headless on Chrome (Windows):
  set BROWSER=chrome
  set HEADLESS=true
  pytest

- Run all tests headless on Chrome (macOS/Linux):
  export BROWSER=chrome
  export HEADLESS=true
  pytest

CI tips
- Use the same pytest commands in your CI pipeline.
- Store reports in a folder (e.g. `reports/`) and archive them from CI.
- Use pytest -n auto for faster feedback when parallelism is safe.

Troubleshooting
- If a web driver is missing, install the matching driver (or use webdriver-manager if included in requirements).
- For permission issues on Unix, ensure venv and driver executables are executable.

## Reports and artifacts

- JUnit XML (useful for CI):

```
pytest --junitxml=results.xml
```

- HTML report (if pytest-html installed):

```
pip install pytest-html
pytest --html=report.html
```

## Running a specific browser via environment variable

You can add a simple env var usage in fixtures. Example:

```
set BROWSER=chrome
pytest
```

and read `BROWSER` in your fixture to choose Chrome or Firefox.

## Debugging tips

- If a test can't find an element: check locators and increase waits (explicit waits recommended).
- If driver fails to start: verify chromedriver/geckodriver version matches browser.
- If tests intermittently fail: add explicit waits, avoid brittle locators.

## Continuous Integration

- Use the same venv + pip install steps in your CI job.
- Use webdriver-manager or install drivers in CI image.
- Collect test artifacts with `--junitxml` and optional HTML reports.

## Common commands summary (Windows)

```
cd C:\Projects\portfolio\automation-portfolio\ui-selenium-python
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt   # or pip install selenium pytest webdriver-manager
set HEADLESS=1
pytest -q --junitxml=results.xml
```

## Troubleshooting quick list

- "ModuleNotFoundError": ensure venv activated and requirements installed.
- "chromedriver not found": use webdriver-manager or put chromedriver.exe on PATH.
- Permissions/blocked downloads: run PowerShell/Command Prompt as administrator if needed.

