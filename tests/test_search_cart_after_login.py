import allure
from utils.helpers import generate_random_user
from utils.logger import get_logger
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_signup_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage

logger = get_logger("test_search_cart_after_login")


@allure.feature("Search Cart after Login")
@allure.story("Search products and verify cart after login")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_products_and_verify_cart(driver):

    logger.info("===== Test started: Search products and verify cart after login =====")

    # -------- Test Data --------
    product_name = "Tshirt"
    user = generate_random_user()
    logger.info(f"Product to search: {product_name}")
    logger.info(f"Generated random user for test: {user['email']}")

    # -------- Page Objects --------
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    auth = SignupLoginPage(driver)
    account = AccountCreationPage(driver)

    with allure.step("Launch application"):
        logger.info("Launching AutomationExercise application")
        home.open()
        home.verify_home_page_visibility()

    with allure.step("Navigate to Products Page"):
        logger.info("Navigating to Products page")
        home.click_products()

    with allure.step("Search for product"):
        logger.info(f"Searching for product: {product_name}")
        products.search_product(product_name)

    with allure.step("Verify searched products are visible"):
        logger.info("Verifying searched products visibility")
        products.verify_searched_products_visible()

    with allure.step("Add all searched products to cart"):
        logger.info("Adding all searched products to cart")
        products.add_all_searched_products_to_cart()

    with allure.step("Verify products are visible in cart before login"):
        logger.info("Verifying products in cart before login")
        cart.click_cart()
        cart.verify_cart_page()
        cart.verify_products_present_in_cart()

    with allure.step("Register a new user"):
        logger.info("Registering a new user from cart page")
        cart.click_signup_login()
        auth.signup(user["name"], user["email"])
        account.fill_account_details(user["password"])
        account.create_account()
        account.verify_account_created()

    with allure.step("Verify user is logged in"):
        logger.info("Verifying user is logged in")
        auth.verify_login()

    with allure.step("Logout from application"):
        logger.info("Logging out from application")
        home.click_logout()

    with allure.step("Login with existing credentials"):
        logger.info("Logging in with existing user credentials")
        auth.login(user["email"], user["password"])

    with allure.step("Verify cart after login"):
        logger.info("Verifying cart contents after login")
        cart.click_cart()
        cart.verify_products_present_in_cart()

    logger.info("===== Test completed successfully: Search products and verify cart after login =====")
