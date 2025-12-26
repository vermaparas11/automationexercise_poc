import allure
from utils.helpers import generate_random_user
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_signup_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

@allure.feature("Order")
@allure.story("Download invoice after purchase")
@allure.severity(allure.severity_level.CRITICAL)
def test_download_invoice(driver):

   # -----------Test Data -----------
    user = generate_random_user()

   #------------Page Objects---------
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    auth = SignupLoginPage(driver)
    account = AccountCreationPage(driver)
    checkout = CheckoutPage(driver)
    payment = PaymentPage(driver)

    with allure.step("launch application and verify home page"):
       home.open()
       home.verify_home_page_visibility()

    with allure.step("Navigate to Products page"):
        home.click_products()

    with allure.step("Add products to cart"):
        products.add_first_product()
        products.add_second_product()

    with allure.step("Navigate to Cart page"):
        cart.click_cart()
        cart.verify_cart_page()

    with allure.step("Proceed to checkout"):
        cart.click_proceed_to_checkout()

    with allure.step("Navigate to signup/ Login page"):
        cart.click_register_login()
        assert "login" in driver.current_url.lower()

    with allure.step("Register a new user"):
        auth.signup(user["name"], user["email"])

    with allure.step("Fill Account Details and Create account"):
        account.fill_account_details(user["password"])
        account.create_account()
        account.verify_account_created()

    with allure.step("verify user is logged in"):
        auth.verify_login()

    with allure.step("Navigate back to Cart and proceed to checkout"):
        cart.click_cart()
        cart.click_proceed_to_checkout()

    with allure.step("verify Address details and review order"):
        checkout.verify_address_details()

    with allure.step(" Enter Order Comment and Place Order"):
        checkout.enter_comment("test order placed via automation")
        checkout.place_order()

    with allure.step("Enter payment details and confirm order"):
        payment.enter_payment_details()
        payment.confirm_order()

    with allure.step("Verify Successful order placement"):
        payment.verify_order_success_message()

    with allure.step("Download invoice and verify it is downloaded"):
        payment.download_invoice()
        payment.verify_invoice_downloaded()

    with allure.step("Delete account and verify deletion"):
        payment.delete_account()
        payment.verify_account_deleted()

