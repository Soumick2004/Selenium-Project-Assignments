from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//h2[contains(normalize-space(), 'Searched Products')]"
    )

    CONTINUE_SHOPPING = (
        By.XPATH,
        "//button[contains(normalize-space(), 'Continue Shopping')]"
    )

    VIEW_CART = (
        By.XPATH,
        "//u[normalize-space()='View Cart']/.."
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def search_product(self, product):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )

        search_box.clear()
        search_box.send_keys(product)

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCHED_PRODUCTS)
        )

    def add_product_to_cart(self, product):
        add_to_cart = (
            By.XPATH,
            f"//div[contains(@class,'productinfo')]"
            f"[.//p[normalize-space()='{product}']]"
            f"//a[contains(@class,'add-to-cart')]"
        )

        element = self.wait.until(
            EC.presence_of_element_located(add_to_cart)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()

    def view_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.VIEW_CART)
        ).click()