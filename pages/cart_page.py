from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    Cart_Rows = (By.XPATH, "//tr[contains(@id, 'product')]")
    Product_Price = (By.XPATH, ".//td[@class='cart_price']/p")
    Product_Quantity = (By.XPATH, ".//td[@class='cart_quantity']/button")
    Product_Total = (By.XPATH, ".//td[@class = 'cart_total']/p")

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