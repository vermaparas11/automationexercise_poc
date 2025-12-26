from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    Address_Details = (By.XPATH, "//h2[text()='Address Details']")
    Review_Order = (By.XPATH, "//h2[text()='Review Your Order']")
    Comment_Text = (By.XPATH, "//textarea[@name='message']")
    Place_Order_Button = (By.XPATH, "//a[text()='Place Order']")

    def verify_address_details(self):
        self.wait.until(
            EC.visibility_of_element_located(self.Address_Details)
        )

    def verify_order_review(self):
        self.wait.until(
            EC.visibility_of_element_located(self.Review_Order)
        )

    def enter_comment(self, comment):
        textarea = self.wait.until(
            EC.presence_of_element_located(self.Comment_Text)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", textarea
        )
        textarea.send_keys(comment)

    def place_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.Place_Order_Button)
        ).click()