from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductsPage(BasePage):

    First_Product = (By.XPATH, "(//div[@class = 'product-image-wrapper'])[1]")
    Second_Product = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")

    Add_to_cart = (By.XPATH, ".//a[contains(@class, 'add-to-cart')]")

    Continue_Shopping = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    View_Cart = (By.XPATH, "//u[text()='View Cart']")

    Search_Input = (By.ID, "search_product")
    Search_Button =(By.ID, "submit_search")
    Searched_Products_Title = (By.XPATH, "//h2[text()='Searched Products']")
    Search_Result = (By.XPATH, "//div[@class='product-image-wrapper']")
    Add_To_Cart_Btn = (By.XPATH, ".//a[contains(@class,'add-to-cart')]")

    def add_product(self, product_locator, go_to_cart =False):
        product = self.scroll_into_view(product_locator)
        self.hover(product_locator)

        add_btn = product.find_element(*self.Add_to_cart)
        self.driver.execute_script("arguments[0].click();", add_btn)

        if go_to_cart:
            self.click(self.View_Cart)
        else:
            self.click(self.Continue_Shopping)


    def add_first_product(self):
        self.add_product(self.First_Product)

    def add_second_product(self):
        self.add_product(self.Second_Product, go_to_cart=True)

    def search_product(self, product_name):
        self.wait.until(
            EC.visibility_of_element_located(self.Search_Input)
        ).send_keys(product_name)

        self.driver.find_element(*self.Search_Button).click()

    def verify_searched_products_visible(self):
        self.wait.until(
            EC.visibility_of_element_located(self.Searched_Products_Title)
        )

        results = self.wait.until(
            EC.presence_of_all_elements_located(self.Search_Result)
        )
        assert len(results) > 0

    def add_all_searched_products_to_cart(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.Search_Result)
        )

        total_products = len(products)

        for index, product in enumerate(products):
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", product
            )


            add_btn = product.find_element(*self.Add_To_Cart_Btn)
            self.driver.execute_script("arguments[0].click();", add_btn)

            # Handle last product
            if index < total_products - 1:
                self.driver.find_element(
                    By.XPATH, "//button[contains(text(),'Continue Shopping')]"
                ).click()

