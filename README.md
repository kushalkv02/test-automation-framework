# Test Automation Framework with Playwright, PyTest & CI/CD

A scalable and production-ready **end-to-end test automation framework** built using **Playwright and PyTest**, featuring **data-driven testing, Allure reporting, CI/CD integration, and a Streamlit analytics dashboard**.

---

## Project Overview

This project demonstrates a complete **automation testing ecosystem** similar to what is used in real-world QA/SDET roles. It automates web application testing, generates detailed reports, and visualizes test analytics.

---

## Features

* ✅ **Page Object Model (POM)** for clean and maintainable code
* ✅ **Data-Driven Testing** using JSON
* ✅ **Parallel Test Execution** with PyTest
* ✅ **Allure Reporting** with step-level insights
* ✅ **Screenshot Capture on Failure**
* ✅ **CI/CD Pipeline** using GitHub Actions
* ✅ **Streamlit Dashboard** for test analytics
* ✅ **Headless Execution** for CI environments

---

## Project Structure

```
test-automation-framework/
│
├── tests/                # Test cases
├── pages/                # Page Object Model classes
├── utils/                # Utilities (data loader, logger)
├── test_data/            # JSON test data
├── reports/              # Allure & JSON reports
├── screenshots/          # Failure screenshots
│
├── conftest.py           # Fixtures & hooks
├── pytest.ini            # PyTest configuration
├── requirements.txt      # Dependencies
├── dashboard.py          # Streamlit dashboard
└── .github/workflows/    # CI/CD pipeline
```

---

## Tech Stack

* **Python**
* **PyTest**
* **Playwright**
* **Allure Reports**
* **Streamlit**
* **GitHub Actions (CI/CD)**

---

## Getting Started

### 1️⃣ Clone Repository

```
git clone https://github.com/<your-username>/test-automation-framework.git
cd test-automation-framework
```

---

### 2️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

```
pytest -v
```

---

## Generate Allure Report

```
pytest --alluredir=reports
allure serve reports
```

---

## Run Test Analytics Dashboard

```
pytest --json-report --json-report-file=reports/report.json
streamlit run dashboard.py
```

---

## CI/CD Pipeline

* Automated test execution on every push
* Configured using **GitHub Actions**
* Runs in headless mode for CI environment

👉 Check the **Actions tab** in the repository to view pipeline runs.

---

## Demo Workflow

1. Run automation tests
2. Generate Allure report
3. View test execution results
4. Launch Streamlit dashboard
5. Analyze test metrics

---

## Key Highlights

* Designed using **industry best practices**
* Modular and scalable architecture
* Real-world automation scenarios (login testing)
* Integrated analytics for better decision-making

---

## Resume Description

> Developed a scalable Playwright-based automation framework using PyTest and Page Object Model, implementing data-driven testing and integrating Allure reporting; configured CI/CD pipelines using GitHub Actions and built a Streamlit dashboard for real-time test analytics.

---

## Future Enhancements

* 🔹 Dockerize the framework
* 🔹 Add API testing module
* 🔹 Integrate cloud testing (BrowserStack)
* 🔹 Add test coverage tracking

---

## Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## Contact

If you have any questions or feedback, feel free to reach out!

---
If you found this project useful, consider giving it a star!
