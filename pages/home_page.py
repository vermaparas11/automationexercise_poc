from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class HomePage(BasePage):

    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    LOGOUT = (By.XPATH, "//a[contains(text(),'Logout')]")
    LOGGED_IN_AS = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    @allure.step("Open AutomationExercise home page")
    def open(self):
        self.logger.info("Navigating to AutomationExercise home page")
        self.driver.get("https://automationexercise.com")
        self.logger.info("Home page opened successfully")

    @allure.step("Verify home page is visible")
    def verify_home_page_visibility(self):
        self.logger.info("Verifying home page visibility using page title")
        assert self.driver.title != "", "Home page title is empty"
        self.logger.info(f"Home page title verified: {self.driver.title}")

    @allure.step("Click Products button")
    def click_products(self):
        self.logger.info("Clicking on Products button from home page")
        self.click(self.PRODUCTS_BUTTON)

    @allure.step("Logout from application")
    def click_logout(self):
        self.logger.info("Waiting for user to be logged in (Logged in as visible)")
        self.wait.until(
            EC.presence_of_element_located(self.LOGGED_IN_AS)
        )

        self.logger.info("Clicking on Logout button")
        logout = self.wait.until(
            EC.presence_of_element_located(self.LOGOUT)
        )
        self.driver.execute_script("arguments[0].click();", logout)
        self.logger.info("Logout action performed successfully")



