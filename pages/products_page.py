from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    First_Product = (By.XPATH, "(//div[@class = 'product-image-wrapper'])[1]")
    Second_Product = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")

    Add_to_cart = (By.XPATH, ".//a[contains(@class, 'add-to-cart')]")

    Continue_Shopping = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    View_Cart = (By.XPATH, "//u[text()='View Cart']")

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

