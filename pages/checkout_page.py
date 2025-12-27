from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):

    ADDRESS_DETAILS = (By.XPATH, "//h2[text()='Address Details']")
    REVIEW_ORDER = (By.XPATH, "//h2[text()='Review Your Order']")
    COMMENT_TEXT = (By.XPATH, "//textarea[@name='message']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[text()='Place Order']")

    # ---------------- Verifications ----------------

    @allure.step("Verify address details section is visible")
    def verify_address_details(self):
        self.logger.info("Verifying Address Details section is visible on checkout page")
        self.wait.until(
            EC.visibility_of_element_located(self.ADDRESS_DETAILS)
        )
        self.logger.info("Address Details section verified successfully")

    @allure.step("Verify review order section is visible")
    def verify_order_review(self):
        self.logger.info("Verifying Review Your Order section is visible on checkout page")
        self.wait.until(
            EC.visibility_of_element_located(self.REVIEW_ORDER)
        )
        self.logger.info("Review Your Order section verified successfully")

    # ---------------- Actions ----------------

    @allure.step("Enter order comment")
    def enter_comment(self, comment):
        self.logger.info("Entering comment in order comment text area")

        textarea = self.wait.until(
            EC.presence_of_element_located(self.COMMENT_TEXT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", textarea
        )
        textarea.send_keys(comment)

        self.logger.info("Order comment entered successfully")

    @allure.step("Place the order")
    def place_order(self):
        self.logger.info("Clicking on Place Order button")

        self.wait.until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        ).click()

        self.logger.info("Place Order button clicked successfully")
