import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class PaymentPage(BasePage):

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")

    PAY_AND_CONFIRM = (By.ID, "submit")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]")

    DOWNLOAD_INVOICE = (By.XPATH, "//a[text()='Download Invoice']")
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")
    DELETE_ACCOUNT = (By.XPATH, "//a[text()=' Delete Account']")
    ACCOUNT_DELETED = (By.XPATH, "//b[text()='Account Deleted!']")

    # ---------------- Payment Details ----------------

    @allure.step("Enter payment details")
    def enter_payment_details(self):
        self.logger.info("Entering payment details (card data masked)")

        self.wait.until(
            EC.visibility_of_element_located(self.NAME_ON_CARD)
        ).send_keys("Test User")

        self.driver.find_element(*self.CARD_NUMBER).send_keys("4111111111111111")
        self.driver.find_element(*self.CVC).send_keys("123")
        self.driver.find_element(*self.EXPIRY_MONTH).send_keys("12")
        self.driver.find_element(*self.EXPIRY_YEAR).send_keys("2027")

        self.logger.info("Payment details entered successfully")

    # ---------------- Confirm Order ----------------

    @allure.step("Confirm order and complete payment")
    def confirm_order(self):
        self.logger.info("Attempting to confirm order")

        pay_btn = self.wait.until(
            EC.presence_of_element_located(self.PAY_AND_CONFIRM)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", pay_btn
        )
        self.logger.info("Pay & Confirm button scrolled into view")

        # JS click used to bypass advertisement iframe
        self.driver.execute_script(
            "arguments[0].click();", pay_btn
        )
        self.logger.info("Order confirmed using JavaScript click")

    # ---------------- Verification ----------------

    @allure.step("Verify order success message")
    def verify_order_success_message(self):
        self.logger.info("Verifying order success confirmation message")

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        self.logger.info("Order success message verified successfully")

    # ---------------- Invoice Download ----------------

    @allure.step("Download invoice")
    def download_invoice(self):
        self.logger.info("Clicking Download Invoice button")

        self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_INVOICE)
        ).click()

        self.logger.info("Download Invoice button clicked")

    @allure.step("Verify invoice is downloaded")
    def verify_invoice_downloaded(self, timeout=10):
        self.logger.info(
            f"Verifying invoice download in Downloads folder (timeout={timeout}s)"
        )

        download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        end_time = time.time() + timeout

        while time.time() < end_time:
            files = os.listdir(download_dir)
            if any("invoice" in f.lower() for f in files):
                self.logger.info("Invoice file detected successfully")
                return True
            time.sleep(1)

        self.logger.error("Invoice file was not downloaded within timeout")
        raise AssertionError("Invoice file was not downloaded")

    # ---------------- Account Deletion ----------------

    @allure.step("Delete user account")
    def delete_account(self):
        self.logger.info("Initiating account deletion")

        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_ACCOUNT)
        ).click()

        self.logger.info("Delete Account button clicked")

    @allure.step("Verify account is deleted successfully")
    def verify_account_deleted(self):
        self.logger.info("Verifying account deletion confirmation")

        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_DELETED)
        )

        self.logger.info("Account deleted successfully")

