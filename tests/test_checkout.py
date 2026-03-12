import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import read_config

config = read_config()


@pytest.mark.sanity
def test_complete_checkout(driver, logger):
    """
    Sanity Test
    Verify end-to-end checkout flow with structured logging
    """

    logger.info(f"Navigating to base URL: {config['base_url']}")
    driver.get(config["base_url"])

    login_page = LoginPage(driver)
    logger.info(f"Logging in with username: {config['username']}")
    login_page.login(config["username"], config["password"])
    logger.info("Login successful")

    products_page = ProductsPage(driver)
    logger.info("Adding backpack to cart")
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()
    logger.info("Navigated to cart page")

    cart_page = CartPage(driver)
    logger.info("Initiating checkout")
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    logger.info("Filling checkout information")
    checkout_page.fill_checkout_info("Shantappa", "Bajare", "585102")

    logger.info("Finishing order")
    checkout_page.finish_order()

    success_message = checkout_page.get_success_message()
    logger.info(f"Checkout success message received: {success_message}")

    assert "thank you for your order" in success_message.lower()
    logger.info("Complete checkout test passed ✅")