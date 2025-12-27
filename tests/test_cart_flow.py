import allure
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger("test_cart_flow")


@allure.feature("Cart")
@allure.story("Add products and verify cart details")
def test_add_products_and_verify_cart(driver):

    logger.info("===== Test started: Add products and verify cart =====")

    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    with allure.step("Launch application"):
        logger.info("Launching AutomationExercise application")
        home.open()
        home.verify_home_page_visibility()

    with allure.step("Navigate to products page"):
        logger.info("Navigating to Products page")
        home.click_products()

    with allure.step("Add first and second product to cart"):
        logger.info("Adding first product to cart")
        products.add_first_product()

        logger.info("Adding second product to cart")
        products.add_second_product()

    with allure.step("Verify cart has two products"):
        logger.info("Verifying cart contains exactly 2 products")
        cart.verify_products_added(expected_count=2)

    with allure.step("Verify price, quantity and total"):
        logger.info("Verifying price, quantity and total for all cart items")
        cart.verify_price_quantity_total()

    logger.info("===== Test completed successfully: Add products and verify cart =====")

