import json
import pytest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.screenshot import capture_screenshot


with open("config/config.json") as file:
    config = json.load(file)

with open("data/test_data.json") as file:
    test_data = json.load(file)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.get(config["url"])

    yield driver

    driver.quit()


def test_purchase_flow(driver):
    try:
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.login(
            test_data["email"],
            test_data["password"]
        )

        assert login_page.is_logged_in()

        home_page.open_products()

        products_page.search_product(
            test_data["product"]
        )

        products_page.add_product_to_cart(
            test_data["product"]
        )

        products_page.continue_shopping()

        cart_page.open_cart()

        product_name = cart_page.get_product_name()
        quantity = cart_page.get_quantity()

        assert test_data["product"].lower() in product_name.lower()

        print("Product:", product_name)
        print("Quantity:", quantity)

        cart_page.proceed_to_checkout()

        checkout_page.verify_checkout_page()

        checkout_page.enter_comment(
            "Please deliver the order carefully."
        )

        checkout_page.place_order()

        checkout_page.enter_payment_details(
            test_data["name_on_card"],
            test_data["card_number"],
            test_data["cvc"],
            test_data["expiry_month"],
            test_data["expiry_year"]
        )

        checkout_page.pay_and_confirm()

        checkout_page.verify_order_success()

        print("Order placed successfully!")

    except Exception:
        capture_screenshot(
            driver,
            "purchase_failure"
        )
        raise