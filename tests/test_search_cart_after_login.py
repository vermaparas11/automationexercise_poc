import allure
from utils.helpers import generate_random_user
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_signup_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage

@allure.feature("Search Cart after Login")
@allure.story("Search products and verify cart after login")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_products_and_verify_cart(driver):

    #------Test Data-----------
    product_name = "Tshirt"
    user = generate_random_user()

    #-------Page Objects ------
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    auth = SignupLoginPage(driver)
    account = AccountCreationPage(driver)

    with allure.step("Launch application"):
        home.open()
        home.verify_home_page_visibility()

    with allure.step("Navigate to Products Page"):
        home.click_products()

    with allure.step("Search for Product"):
        products.search_product(product_name)

    with allure.step("Verify Searched products are visible"):
        products.verify_searched_products_visible()

    with allure.step("Add all searched products to cart"):
        products.add_all_searched_products_to_cart()

    with allure.step("Verify products are visible in cart before login"):
        cart.click_cart()
        cart.verify_cart_page()
        cart.verify_products_present_in_cart()

    with allure.step("Register a new user"):
        cart.click_signup_login()
        auth.signup(user["name"], user["email"])
        account.fill_account_details(user["password"])
        account.create_account()
        account.verify_account_created()

    with allure.step("verify user logged in"):
        auth.verify_login()

    with allure.step("Logout from application"):
        home.click_logout()

    with allure.step("login  with existing credentials"):
        auth.login(user["email"], user["password"])

    with allure.step("Verify Cart after login"):
        cart.click_cart()
        cart.verify_products_present_in_cart()