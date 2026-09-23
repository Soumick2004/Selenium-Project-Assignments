from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    SIGNUP_LOGIN = (By.LINK_TEXT, "Signup / Login")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Login to your account']")
    EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN = (By.XPATH, "//a[contains(.,'Logged in as')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_HEADER)
        )

    def login(self, email, password):
        self.open_login()

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN)
        )

    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN)
        ).is_displayed()