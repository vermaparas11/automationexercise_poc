import allure
from utils.helpers import generate_random_user
from utils.logger import get_logger
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_signup_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

logger = get_logger("test_invoice")


@allure.feature("Order")
@allure.story("Download invoice after purchase")
@allure.severity(allure.severity_level.CRITICAL)
def test_download_invoice(driver):

    logger.info("===== Test started: Download invoice after purchase =====")

    # ----------- Test Data -----------
    user = generate_random_user()
    logger.info(f"Generated random user for test: {user['email']}")

    # ----------- Page Objects --------
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    auth = SignupLoginPage(driver)
    account = AccountCreationPage(driver)
    checkout = CheckoutPage(driver)
    payment = PaymentPage(driver)

    with allure.step("Launch application and verify home page"):
        logger.info("Launching AutomationExercise application")
        home.open()
        home.verify_home_page_visibility()

    with allure.step("Navigate to Products page"):
        logger.info("Navigating to Products page")
        home.click_products()

    with allure.step("Add products to cart"):
        logger.info("Adding products to cart")
        products.add_first_product()
        products.add_second_product()

    with allure.step("Navigate to Cart page"):
        logger.info("Navigating to Cart page")
        cart.click_cart()
        cart.verify_cart_page()

    with allure.step("Proceed to checkout"):
        logger.info("Proceeding to checkout from cart")
        cart.click_proceed_to_checkout()

    with allure.step("Navigate to Signup / Login page"):
        logger.info("Navigating to Signup / Login page")
        cart.click_register_login()
        assert "login" in driver.current_url.lower(), "Login page URL not detected"
        logger.info("Signup / Login page verified via URL")

    with allure.step("Register a new user"):
        logger.info("Registering a new user")
        auth.signup(user["name"], user["email"])

    with allure.step("Fill account details and create account"):
        logger.info("Filling account details and creating account")
        account.fill_account_details(user["password"])
        account.create_account()
        account.verify_account_created()

    with allure.step("Verify user is logged in"):
        logger.info("Verifying logged-in state")
        auth.verify_login()

    with allure.step("Navigate back to Cart and proceed to checkout"):
        logger.info("Navigating back to Cart and proceeding to checkout")
        cart.click_cart()
        cart.click_proceed_to_checkout()

    with allure.step("Verify address details and review order"):
        logger.info("Verifying address details and order review section")
        checkout.verify_address_details()

    with allure.step("Enter order comment and place order"):
        logger.info("Entering order comment and placing order")
        checkout.enter_comment("test order placed via automation")
        checkout.place_order()

    with allure.step("Enter payment details and confirm order"):
        logger.info("Entering payment details and confirming order")
        payment.enter_payment_details()
        payment.confirm_order()

    with allure.step("Verify successful order placement"):
        logger.info("Verifying successful order placement")
        payment.verify_order_success_message()

    with allure.step("Download invoice and verify it is downloaded"):
        logger.info("Downloading invoice and verifying download")
        payment.download_invoice()
        payment.verify_invoice_downloaded()

    with allure.step("Delete account and verify deletion"):
        logger.info("Deleting user account and verifying deletion")
        payment.delete_account()
        payment.verify_account_deleted()

    logger.info("===== Test completed successfully: Download invoice after purchase =====")


