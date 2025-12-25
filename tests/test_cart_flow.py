import allure
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@allure.feature("cart")
@allure.story("Add products and verify cart details")
def test_add_products_and_verify_cart(driver):

    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    with allure.step("Launch application"):
        home.open()
        home.verify_home_page_visibility()

    with allure.step("Navigate to products page"):
        home.click_products()

    with allure.step("Add first and second product to cart"):
        products.add_first_product()
        products.add_second_product()

    with allure.step("verify cart has two products"):
        cart.verify_products_added(expected_count=2)

    with allure.step("verify price, quantity and total"):
        cart.verify_price_quantity_total()
