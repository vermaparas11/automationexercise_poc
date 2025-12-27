from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class AccountCreationPage(BasePage):

    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")

    CREATE_ACCOUNT = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE = (By.XPATH, "//a[@data-qa='continue-button']")

    # ---------------- Account Details ----------------

    @allure.step("Fill account details")
    def fill_account_details(self, password):
        self.logger.info("Filling account details for new user")

        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.logger.info("Password entered (masked)")

        self.driver.find_element(*self.FIRST_NAME).send_keys("Test")
        self.driver.find_element(*self.LAST_NAME).send_keys("User")
        self.driver.find_element(*self.ADDRESS).send_keys("Test Address")
        self.driver.find_element(*self.STATE).send_keys("MP")
        self.driver.find_element(*self.CITY).send_keys("Bhopal")
        self.driver.find_element(*self.ZIPCODE).send_keys("462001")
        self.driver.find_element(*self.MOBILE).send_keys("999999999")

        self.logger.info(
            "Personal and address details filled successfully "
            "(First Name, Last Name, Address, City, State, Zipcode, Mobile)"
        )

    # ---------------- Create Account ----------------

    @allure.step("Create user account")
    def create_account(self):
        self.logger.info("Initiating account creation")

        button = self.wait.until(
            EC.presence_of_element_located(self.CREATE_ACCOUNT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", button
        )
        self.logger.info("Create Account button scrolled into view")

        self.driver.execute_script("arguments[0].click();", button)
        self.logger.info("Create Account button clicked")

    # ---------------- Verification ----------------

    @allure.step("Verify account is created successfully")
    def verify_account_created(self):
        self.logger.info("Verifying account creation success message")

        account_created_msg = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED)
        )
        assert account_created_msg is not None, "Account creation message not displayed"

        self.logger.info("Account successfully created")

        self.driver.find_element(*self.CONTINUE).click()
        self.logger.info("Clicked Continue after account creation")
