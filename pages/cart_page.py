from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class CartPage(BasePage):
    Cart_Button = (By.XPATH, "//a[@href='/view_cart']")
    Cart_Page_Title = (By.XPATH, "//li[@class ='active' and contains(text(), 'Shopping Cart')]")
    Cart_Rows = (By.XPATH, "//tr[contains(@id, 'product')]")
    Product_Price = (By.XPATH, ".//td[@class='cart_price']/p")
    Product_Quantity = (By.XPATH, ".//td[@class='cart_quantity']/button")
    Product_Total = (By.XPATH, ".//td[@class = 'cart_total']/p")
    Proceed_to_Checkout = (By.XPATH, "//a[text()='Proceed To Checkout']")
    Register_Login = (By.XPATH, "//u[text()='Register / Login']")
    Cart_Products =(By.XPATH, "//tr[contains(@id,'product')]")
    Signup_Login = (By.XPATH, "//a[contains(text(),'Signup')]")
    def click_cart(self):
        """
        Navigates to Cart Page

        """
        self.wait.until(EC.element_to_be_clickable(self.Cart_Button)).click()

    def verify_cart_page(self):
        """
        Verifies Cart page is displayed
        """
        self.wait.until(EC.visibility_of_element_located(self.Cart_Page_Title))

    def verify_products_added(self, expected_count):
        rows = self.driver.find_elements(*self.Cart_Rows)
        assert len(rows) == expected_count

    def verify_price_quantity_total(self):
        rows = self.driver.find_elements(*self.Cart_Rows)
        for row in rows:
            price = row.find_element(*self.Product_Price).text
            qty = row.find_element(*self.Product_Quantity).text
            total = row.find_element(*self.Product_Total).text

            assert price != ""
            assert qty == "1"
            assert total != ""

    def click_proceed_to_checkout(self):
        self.wait.until(EC.visibility_of_element_located(self.Proceed_to_Checkout)).click()

    def click_register_login(self):
        self.wait.until(EC.visibility_of_element_located(self.Register_Login)).click()

    def verify_products_present_in_cart(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.Cart_Products)
        )
        assert len(products) > 0

    def click_signup_login(self):
        """
        Navigates to Signup / Login page
        """
        signup_login = self.wait.until(
            EC.presence_of_element_located(self.Signup_Login)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", signup_login
        )
        self.driver.execute_script("arguments[0].click();", signup_login)