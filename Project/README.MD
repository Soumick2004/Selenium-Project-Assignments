# Selenium E-Commerce Purchase Automation

## Overview

This project automates an end-to-end e-commerce purchase workflow using Selenium WebDriver with Python and Pytest.

The automation follows the Page Object Model (POM) design pattern and covers user login, product search, cart operations, checkout, payment, and order confirmation on the Automation Exercise practice website.

Website: https://automationexercise.com/

## Project Title

Selenium E-Commerce Purchase Automation

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- JSON
- Page Object Model (POM)

## Project Structure

```text
Project/
│
├── config/
│   └── config.json
│
├── data/
│   └── test_data.json
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── screenshots/
│
├── reports/
│
├── tests/
│   ├── __init__.py
│   └── test_purchase.py
│
├── utils/
│   ├── __init__.py
│   └── screenshot.py
│
└── requirements.txt
```
## Test Scenario

The automated test performs the following end-to-end workflow:

1. Open Automation Exercise.
2. Navigate to the Login page.
3. Login using registered user credentials.
4. Verify that the user is logged in.
5. Navigate to the Products page.
6. Search for a product.
7. Add the searched product to the cart.
8. Continue shopping.
9. Open the cart.
10. Verify the product name and quantity.
11. Proceed to checkout.
12. Verify the checkout page.
13. Enter an order comment.
14. Place the order.
15. Enter payment details.
16. Confirm the payment.
17. Verify successful order placement.

AutomationExercise documents a similar login-before-checkout purchase workflow in its test cases.

## Page Object Model

The project uses the Page Object Model to separate page-specific locators and actions from the test logic.

### LoginPage

Handles:

- Opening the Login page
- Entering email and password
- Clicking the Login button
- Verifying the logged-in state

### HomePage

Handles:

- Navigating to the Products page

### ProductsPage

Handles:

- Searching for a product
- Adding the selected product to the cart
- Continuing shopping

### CartPage

Handles:

- Opening the cart
- Retrieving the product name
- Retrieving the product quantity
- Proceeding to checkout

### CheckoutPage

Handles:

- Verifying the checkout page
- Entering the order comment
- Placing the order
- Entering payment information
- Confirming payment
- Verifying successful order placement

## Test Data

Test data is stored separately in:

`data/test_data.json`

Example:

```json
{
    "email": "YOUR_REGISTERED_EMAIL",
    "password": "YOUR_REGISTERED_PASSWORD",
    "product": "Blue Top",
    "quantity": 2,
    "name_on_card": "Test User",
    "card_number": "4111111111111111",
    "cvc": "123",
    "expiry_month": "12",
    "expiry_year": "2030"
}