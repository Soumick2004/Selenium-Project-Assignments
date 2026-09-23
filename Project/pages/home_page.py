from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    PRODUCTS = (By.CSS_SELECTOR, "a[href='/products']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_products(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS)
        ).click()