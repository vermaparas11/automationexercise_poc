from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class ProductsPage(BasePage):

    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")

    ADD_TO_CART = (By.XPATH, ".//a[contains(@class, 'add-to-cart')]")

    CONTINUE_SHOPPING = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    VIEW_CART = (By.XPATH, "//u[text()='View Cart']")

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Searched Products']")
    SEARCH_RESULT = (By.XPATH, "//div[@class='product-image-wrapper']")
    ADD_TO_CART_BTN = (By.XPATH, ".//a[contains(@class,'add-to-cart')]")

    # ---------------- Add Products ----------------

    @allure.step("Add product to cart")
    def add_product(self, product_locator, go_to_cart=False):
        self.logger.info(f"Adding product to cart using locator: {product_locator}")

        product = self.scroll_into_view(product_locator)
        self.hover(product_locator)

        add_btn = product.find_element(*self.ADD_TO_CART)
        self.driver.execute_script("arguments[0].click();", add_btn)
        self.logger.info("Product added to cart")

        if go_to_cart:
            self.logger.info("Navigating to Cart page after adding product")
            self.click(self.VIEW_CART)
        else:
            self.logger.info("Continuing shopping after adding product")
            self.click(self.CONTINUE_SHOPPING)

    @allure.step("Add first product to cart")
    def add_first_product(self):
        self.logger.info("Adding first product to cart")
        self.add_product(self.FIRST_PRODUCT)

    @allure.step("Add second product to cart and go to cart")
    def add_second_product(self):
        self.logger.info("Adding second product to cart and navigating to cart")
        self.add_product(self.SECOND_PRODUCT, go_to_cart=True)

    # ---------------- Search Products ----------------

    @allure.step("Search for product: {product_name}")
    def search_product(self, product_name):
        self.logger.info(f"Searching for product with name: {product_name}")

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        ).send_keys(product_name)

        self.driver.find_element(*self.SEARCH_BUTTON).click()
        self.logger.info("Search submitted successfully")

    @allure.step("Verify searched products are visible")
    def verify_searched_products_visible(self):
        self.logger.info("Verifying 'Searched Products' section is visible")

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCHED_PRODUCTS_TITLE)
        )

        results = self.wait.until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULT)
        )

        self.logger.info(f"Number of searched products found: {len(results)}")
        assert len(results) > 0, "No products found for the search criteria"

    @allure.step("Add all searched products to cart")
    def add_all_searched_products_to_cart(self):
        self.logger.info("Adding all searched products to cart")

        products = self.wait.until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULT)
        )

        total_products = len(products)
        self.logger.info(f"Total searched products to add: {total_products}")

        for index, product in enumerate(products, start=1):
            self.logger.info(f"Adding product {index} of {total_products}")

            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", product
            )

            add_btn = product.find_element(*self.ADD_TO_CART_BTN)
            self.driver.execute_script("arguments[0].click();", add_btn)

            if index < total_products:
                self.logger.info("Clicking Continue Shopping")
                self.driver.find_element(
                    By.XPATH, "//button[contains(text(),'Continue Shopping')]"
                ).click()

        self.logger.info("All searched products added to cart successfully")
