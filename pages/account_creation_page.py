from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AccountCreationPage(BasePage):
    Password = (By.ID, "password")
    Days = (By.ID, "days")
    Months = (By.ID, "months")
    Years = (By.ID, "years")

    First_Name = (By.ID, "first_name")
    Last_Name = (By.ID, "last_name")
    Address = (By.ID, "address1")
    State = (By.ID, "state")
    City = (By.ID, "city")
    Zipcode = (By.ID, "zipcode")
    Mobile = (By.ID, "mobile_number")

    Create_Account = (By.XPATH, "//button[@data-qa='create-account']")
    Account_Created = (By.XPATH, "//b[text()='Account Created!']")
    Continue = (By.XPATH, "//a[@data-qa='continue-button']")

    def fill_account_details(self, password):
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.First_Name).send_keys("Test")
        self.driver.find_element(*self.Last_Name).send_keys("User")
        self.driver.find_element(*self.Address).send_keys("Test Address")
        self.driver.find_element(*self.State).send_keys("MP")
        self.driver.find_element(*self.City).send_keys("Bhopal")
        self.driver.find_element(*self.Zipcode).send_keys("462001")
        self.driver.find_element(*self.Mobile).send_keys("999999999")

    def create_account(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.Create_Account)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def verify_account_created(self):
        assert self.wait.until(EC.visibility_of_element_located(self.Account_Created))
        self.driver.find_element(*self.Continue).click()