from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")

    def open(self):
        self.driver.get("https://automationexercise.com")
    def verify_home_page_visibility(self):
        assert self.driver.title != ""

    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)
