from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class SignupLoginPage(BasePage):

    Signup_Name = (By.XPATH, "//input[@data-qa='signup-name']")
    Signup_Email = (By.XPATH, "//input[@data-qa='signup-email']")
    Signup_Button = (By.XPATH, "//button[@data-qa='signup-button']")

    Login_Email = (By.XPATH, "//input[@data-qa='login-email']")
    Login_Password = (By.XPATH, "//input[@data-qa='login-password']")
    Login_Button = (By.XPATH, "//button[@data-qa='login-button']")

    Logged_In_Text = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def signup(self, name, email):
        self.wait.until(EC.visibility_of_element_located(self.Signup_Name)).send_keys(name)
        self.driver.find_element(*self.Signup_Email).send_keys(email)
        self.driver.find_element(*self.Signup_Button).click()

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.Login_Email)).send_keys(email)
        self.driver.find_element(*self.Login_Password).send_keys(password)
        self.driver.find_element(*self.Login_Button).click()

    def verify_login(self):
        assert self.wait.until(EC.visibility_of_element_located(self.Logged_In_Text))