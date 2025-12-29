pytest
allure serve reports

# AutomationExercise – UI Automation POC

This repository contains an end-to-end UI automation Proof of Concept (POC) for  
https://automationexercise.com using **Python, Pytest, Selenium, and Allure**.

The POC demonstrates a clean automation framework, real-world Selenium handling,
and stable execution of business-critical scenarios.

---

## Tech Stack

- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure Reporting
- WebDriver Manager
- Chrome Browser

---
## Framework Structure

automationexercise-poc/
│
├── tests/
│ ├── test_cart_flow.py
│ ├── test_invoice.py
│ └── test_sanity.py
│
├── pages/
│ ├── base_page.py
│ ├── home_page.py
│ ├── products_page.py
│ ├── cart_page.py
│ ├── login_signup_page.py
│ ├── account_creation_page.py
│ ├── checkout_page.py
│ └── payment_page.py
│
├── utils/
│ ├── driver_factory.py
│ └── helpers.py
│
├── reports/
├── downloads/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

---
## Automated Test Scenarios
### Scenario 1: Add Products in Cart
- Add multiple products
- Verify product count
- Verify price, quantity, and total

### Scenario 2: Download Invoice After Purchase
- Add products to cart
- Signup with a random user
- Complete checkout and payment
- Verify order success
- Download invoice
- Delete account

### Scenario 3: Search Products & Verify Cart After Login

- Search for products
- Add searched products to cart
- Register user
- Logout and login again
- Verify cart items getting displayed after login

Verify cart persistence after login
---

##  How to Run Tests

### Install dependencies
pip install -r requirements.txt

### Run Test
pytest -v

### Generate Allure Report:
allure serve reports

### Generate static report
allure generate reports -o allure-report --clean

---
## Screenshot on Failure
- Screenshots are automatically captured on test failure
- Attached directly to Allure reports
- Implemented using Pytest hooks
---
## Test Data Handling
- Dynamic user creation using random dat
- Ensures tests are independent and repeatable
- No dependency on pre-existing accounts
---

## Author
### Paras Verma
### Senior Test Analyst
### Python | Selenium | Pytest |Automation

---
### Notes
- The logs/, reports/, and virtual environment directories are excluded from version control.



