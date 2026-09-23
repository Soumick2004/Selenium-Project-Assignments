from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART = (By.CSS_SELECTOR, "a[href='/view_cart']")
    CART_HEADER = (
        By.XPATH,
        "//li[contains(@class,'active') and normalize-space()='Cart']"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#cart_info_table .cart_description h4 a"
    )

    QUANTITY = (
        By.CSS_SELECTOR,
        "#cart_info_table .cart_quantity button"
    )

    PROCEED_CHECKOUT = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Proceed To Checkout')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        )

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def get_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY)
        ).text

    def proceed_to_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PROCEED_CHECKOUT)
        ).click()