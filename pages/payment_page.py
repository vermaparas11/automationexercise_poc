import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


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

    def enter_payment_details(self):
        self.wait.until(EC.visibility_of_element_located(self.NAME_ON_CARD)).send_keys("Test User")
        self.driver.find_element(*self.CARD_NUMBER).send_keys("4111111111111111")
        self.driver.find_element(*self.CVC).send_keys("123")
        self.driver.find_element(*self.EXPIRY_MONTH).send_keys("12")
        self.driver.find_element(*self.EXPIRY_YEAR).send_keys("2027")

    def confirm_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PAY_AND_CONFIRM)
        ).click()

    def verify_order_success_message(self):
        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

    def download_invoice(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_INVOICE)
        ).click()

    def verify_invoice_downloaded(self, timeout=10):
        """
        Simple verification:
        checks that any .txt or .pdf file appears in Downloads
        """
        download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        end_time = time.time() + timeout

        while time.time() < end_time:
            files = os.listdir(download_dir)
            if any("invoice" in f.lower() for f in files):
                return True
            time.sleep(1)

        raise AssertionError("Invoice file was not downloaded")

    def delete_account(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_ACCOUNT)
        ).click()

    def verify_account_deleted(self):
        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_DELETED)
        )
