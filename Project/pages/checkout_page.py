from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    ADDRESS_DETAILS = (
        By.XPATH,
        "//h2[normalize-space()='Address Details']"
    )

    COMMENT = (
        By.CSS_SELECTOR,
        "textarea[name='message']"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Place Order')]"
    )

    NAME_ON_CARD = (
        By.CSS_SELECTOR,
        "input[data-qa='name-on-card']"
    )

    CARD_NUMBER = (
        By.CSS_SELECTOR,
        "input[data-qa='card-number']"
    )

    CVC = (
        By.CSS_SELECTOR,
        "input[data-qa='cvc']"
    )

    EXPIRY_MONTH = (
        By.CSS_SELECTOR,
        "input[data-qa='expiry-month']"
    )

    EXPIRY_YEAR = (
        By.CSS_SELECTOR,
        "input[data-qa='expiry-year']"
    )

    PAY_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='pay-button']"
    )

    ORDER_SUCCESS = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Congratulations! Your order has been confirmed!')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_checkout_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.ADDRESS_DETAILS)
        )

    def enter_comment(self, comment):
        self.wait.until(
            EC.visibility_of_element_located(self.COMMENT)
        ).send_keys(comment)

    def place_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PLACE_ORDER)
        ).click()

    def enter_payment_details(
        self,
        name,
        card_number,
        cvc,
        expiry_month,
        expiry_year
    ):
        self.wait.until(
            EC.visibility_of_element_located(self.NAME_ON_CARD)
        ).send_keys(name)

        self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER)
        ).send_keys(card_number)

        self.wait.until(
            EC.visibility_of_element_located(self.CVC)
        ).send_keys(cvc)

        self.wait.until(
            EC.visibility_of_element_located(self.EXPIRY_MONTH)
        ).send_keys(expiry_month)

        self.wait.until(
            EC.visibility_of_element_located(self.EXPIRY_YEAR)
        ).send_keys(expiry_year)

    def pay_and_confirm(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PAY_BUTTON)
        ).click()

    def verify_order_success(self):
        self.wait.until(
            EC.visibility_of_element_located(self.ORDER_SUCCESS)
        )