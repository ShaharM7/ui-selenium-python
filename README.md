# UI Selenium Python Test Suite

This project contains UI automation tests written in Python using Selenium WebDriver.  
The same test suite can be executed:

- Locally (e.g., using Chrome/Firefox on your machine)
- On BrowserStack (cloud browsers and devices)
- Against your own deployed instance of the application

> Adjust paths, commands, and environment variables below to match your setup.

---

## 1. Prerequisites

- Python 3.10+ installed
- `pip` available on PATH
- Google Chrome / Firefox /Edge (for local execution)
- Browser drivers (e.g., ChromeDriver / GeckoDriver) available on PATH or managed by your framework
- Git (optional, for cloning)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Configuration

Use the variables that already ship in `.env`:

| Variable | Purpose |
| --- | --- |
| `NAVIGATION_CONFIG_BASEURL` | Base URL of the app under test. |
| `NAVIGATION_CONFIG_SIGN_IN_ROUTE` | Relative route for sign-in flows. |
| `AWAITER_CONFIG_*` | Synchronization timeouts (timeout, polling, implicit wait, async JS, page load). |
| `BROWSER_OPTIONS_CONFIG_ARGUMENTS` | Extra Chromium arguments applied to every session. |
| `IS_USE_SELENIUM_GRID` | Toggle for your self-hosted Selenium Grid (`true` runs against `SELENIUM_GRID_K8S_CONFIG_URL`). |
| `IS_USE_BROWSER_STACK` | Toggle for BrowserStack runs (uses `REMOTEBROWSER_CONFIG_*`). |
| `SELENIUM_GRID_K8S_CONFIG_URL` | URL of your Selenium Grid hub. |
| `BROWSER_NAME_CONFIG` | Browser name passed to the driver factory (e.g., `chrome`). |
| `REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL` | Remote WebDriver endpoint (defaults to BrowserStack hub and interpolates `BROWSERSTACK_USERNAME` / `BROWSERSTACK_ACCESS_KEY`). |
| `REMOTEBROWSER_CONFIG_OS_NAME` / `REMOTEBROWSER_CONFIG_OS_VERSION` / `REMOTEBROWSER_CONFIG_BROWSER_VERSION` | Desired capabilities for BrowserStack sessions. |

> Copy `.env` to `.env.local` (or export the same keys) and update the values per environment.



## 3. Run Tests Locally

Example overrides:

```bash
NAVIGATION_CONFIG_BASEURL=http://localhost:3000 \
IS_USE_SELENIUM_GRID=false \
IS_USE_BROWSER_STACK=false \
BROWSER_NAME_CONFIG=chrome \
pytest -v
```

If you prefer your own Selenium Grid (e.g., the K8s hub already in `.env`):

```bash
NAVIGATION_CONFIG_BASEURL=http://localhost:3000 \
IS_USE_SELENIUM_GRID=true \
SELENIUM_GRID_K8S_CONFIG_URL=http://<grid-host>:4444 \
pytest -v
```

### 3.1. Using Local Browser

1. Ensure your application is running locally (e.g., `http://localhost:3000`).
2. Set environment variables:

```bash
export TARGET_ENV=local
export BASE_URL=http://localhost:3000
export BROWSER=chrome
export HEADLESS=false
```

3. Run the tests (adapt to your test runner):

```bash
pytest -v
# or
python -m pytest -v
```

### 3.2. Headless Mode

To run in headless mode (useful in CI):

```bash
export HEADLESS=true
pytest -v
```

---

## 4. Run Tests on BrowserStack

1. Export your credentials so the interpolation inside `REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL` works:

```bash
export BROWSERSTACK_USERNAME=<your-user>
export BROWSERSTACK_ACCESS_KEY=<your-key>
```

2. Run the suite with the BrowserStack toggle:

```bash
NAVIGATION_CONFIG_BASEURL=https://your-public-or-tunneled-url.example \
IS_USE_BROWSER_STACK=true \
IS_USE_SELENIUM_GRID=false \
REMOTEBROWSER_CONFIG_OS_NAME=Windows \
REMOTEBROWSER_CONFIG_OS_VERSION=11 \
REMOTEBROWSER_CONFIG_BROWSER_VERSION=latest \
pytest -v
```

3. (Optional) Start BrowserStack Local if the target URL is not publicly reachable.

The driver factory should detect `IS_USE_BROWSER_STACK=true` and instantiate `RemoteWebDriver` using `REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL`.

---

## 5. Run Tests Against Your Hosted Instance

The grid runs on the separate **`selenium-grid-doks`** project, deployed to a DigitalOcean Kubernetes cluster.  
`SELENIUM_GRID_K8S_CONFIG_URL` already contains the public load balancer endpoint of the cluster’s Selenium Grid router (e.g., `http://159.223.250.133:4444`). Use that value whenever you target the hosted instance via Grid.

```bash
# Run against your staging instance via local browser
NAVIGATION_CONFIG_BASEURL=https://staging.example.com \
IS_USE_SELENIUM_GRID=false \
IS_USE_BROWSER_STACK=false \
pytest -v
```

```bash
# Run against the same instance via your DigitalOcean Selenium Grid
NAVIGATION_CONFIG_BASEURL=https://staging.example.com \
IS_USE_SELENIUM_GRID=true \
SELENIUM_GRID_K8S_CONFIG_URL=${SELENIUM_GRID_K8S_CONFIG_URL:-http://159.223.250.133:4444} \
pytest -v
```

```bash
# Run against the instance via BrowserStack
NAVIGATION_CONFIG_BASEURL=https://staging.example.com \
IS_USE_BROWSER_STACK=true \
IS_USE_SELENIUM_GRID=false \
pytest -v
```

Keep credentials, secrets, and any app-specific data outside of the repository; only the documented keys should be overridden per environment.

---

## 6. Typical Folder Structure

```text
ui-selenium-python/
  ├─ tests/
  │   ├─ test_login.py
  │   ├─ test_checkout.py
  │   └─ ...
  ├─ pages/
  │   ├─ login_page.py
  │   └─ ...
  ├─ drivers/ ...
  ├─ requirements.txt
  └─ README.md
```

---

## 7. Extending / Modifying

- Add new tests under `tests/`.
- Add or update page objects under `pages/`.
- Update the driver/config logic (e.g., `driver_factory.py`) to support additional:
  - Browsers
  - Platforms (more BrowserStack capabilities)
  - Environments (e.g., `qa`, `staging`, `prod`)

Keep all environment-specific details in configuration, not in individual tests, so the same tests can run:

- Locally
- On BrowserStack
- On your own instance of the app - in our case - selenium grid that is deployed by GitHub Actions
