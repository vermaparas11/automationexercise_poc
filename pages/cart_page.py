from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class CartPage(BasePage):

    CART_BUTTON = (By.XPATH, "//a[@href='/view_cart']")
    CART_PAGE_TITLE = (By.XPATH, "//li[@class='active' and contains(text(),'Shopping Cart')]")
    CART_ROWS = (By.XPATH, "//tr[contains(@id,'product')]")

    PRODUCT_PRICE = (By.XPATH, ".//td[@class='cart_price']/p")
    PRODUCT_QUANTITY = (By.XPATH, ".//td[@class='cart_quantity']/button")
    PRODUCT_TOTAL = (By.XPATH, ".//td[@class='cart_total']/p")

    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[text()='Proceed To Checkout']")
    REGISTER_LOGIN = (By.XPATH, "//u[text()='Register / Login']")
    CART_PRODUCTS = (By.XPATH, "//tr[contains(@id,'product')]")
    SIGNUP_LOGIN = (By.XPATH, "//a[contains(text(),'Signup') or contains(text(),'Login')]")

    # ---------------- Navigation ----------------

    @allure.step("Navigate to Cart page")
    def click_cart(self):
        self.logger.info("Clicking on Cart button")
        self.click(self.CART_BUTTON)

    @allure.step("Verify Cart page is displayed")
    def verify_cart_page(self):
        self.logger.info("Verifying Cart page title is visible")
        self.wait.until(
            EC.visibility_of_element_located(self.CART_PAGE_TITLE)
        )
        self.logger.info("Cart page displayed successfully")

    # ---------------- Verifications ----------------

    @allure.step("Verify {expected_count} products are added to cart")
    def verify_products_added(self, expected_count):
        rows = self.driver.find_elements(*self.CART_ROWS)
        actual_count = len(rows)
        self.logger.info(
            f"Verifying number of products in cart. "
            f"Expected: {expected_count}, Actual: {actual_count}"
        )
        assert actual_count == expected_count, \
            f"Expected {expected_count} products, but found {actual_count}"

    @allure.step("Verify price, quantity, and total for each product")
    def verify_price_quantity_total(self):
        rows = self.driver.find_elements(*self.CART_ROWS)
        self.logger.info(f"Verifying price, quantity, and total for {len(rows)} products")

        for index, row in enumerate(rows, start=1):
            price = row.find_element(*self.PRODUCT_PRICE).text
            qty = row.find_element(*self.PRODUCT_QUANTITY).text
            total = row.find_element(*self.PRODUCT_TOTAL).text

            self.logger.info(
                f"Product {index} -> Price: {price}, Quantity: {qty}, Total: {total}"
            )

            assert price != "", f"Price is empty for product {index}"
            assert qty == "1", f"Quantity is not 1 for product {index}"
            assert total != "", f"Total is empty for product {index}"

    @allure.step("Verify products are present in cart")
    def verify_products_present_in_cart(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_PRODUCTS)
        )
        count = len(products)
        self.logger.info(f"Number of products present in cart: {count}")
        assert count > 0, "No products found in cart"

    # ---------------- Checkout / Auth ----------------

    @allure.step("Proceed to checkout")
    def click_proceed_to_checkout(self):
        self.logger.info("Clicking Proceed To Checkout button")
        self.click(self.PROCEED_TO_CHECKOUT)

    @allure.step("Click Register / Login from cart")
    def click_register_login(self):
        self.logger.info("Clicking Register / Login link from cart page")
        self.click(self.REGISTER_LOGIN)

    @allure.step("Navigate to Signup / Login page from cart")
    def click_signup_login(self):
        self.logger.info("Navigating to Signup / Login page from cart")
        signup_login = self.wait.until(
            EC.presence_of_element_located(self.SIGNUP_LOGIN)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", signup_login
        )
        self.driver.execute_script(
            "arguments[0].click();", signup_login
        )
        self.logger.info("Signup / Login page navigation successful")