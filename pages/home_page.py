from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    Logout = (By.XPATH, "//a[contains(text(),'Logout')]")
    Logged_In_As = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    def open(self):
        self.driver.get("https://automationexercise.com")
    def verify_home_page_visibility(self):
        assert self.driver.title != ""

    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def click_logout(self):
        self.wait.until(
            EC.presence_of_element_located(self.Logged_In_As)
        )
        logout = self.wait.until(
            EC.presence_of_element_located(self.Logout)
        )
        self.driver.execute_script("arguments[0].click();", logout)


