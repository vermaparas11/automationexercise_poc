from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class SignupLoginPage(BasePage):

    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")

    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    # ---------------- Signup ----------------

    @allure.step("Signup with name: {name} and email: {email}")
    def signup(self, name, email):
        self.logger.info(f"Starting signup with name='{name}', email='{email}'")

        self.wait.until(
            EC.visibility_of_element_located(self.SIGNUP_NAME)
        ).send_keys(name)

        self.driver.find_element(*self.SIGNUP_EMAIL).send_keys(email)
        self.logger.info("Signup name and email entered")

        self.driver.find_element(*self.SIGNUP_BUTTON).click()
        self.logger.info("Signup button clicked")

    # ---------------- Login ----------------

    @allure.step("Login with email: {email}")
    def login(self, email, password):
        self.logger.info(f"Attempting login with email='{email}'")

        self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_EMAIL)
        ).send_keys(email)

        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.logger.info("Login credentials entered (password masked)")

        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.logger.info("Login button clicked")

    # ---------------- Verification ----------------

    @allure.step("Verify user is logged in")
    def verify_login(self):
        self.logger.info("Verifying user login status")
        logged_in_element = self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_TEXT)
        )
        assert logged_in_element is not None, "User is not logged in"
        self.logger.info("User logged in successfully")
