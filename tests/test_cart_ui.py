import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config_reader import read_config
from utils.logger import get_logger

config = read_config()
logger = get_logger()


@pytest.mark.regression
def test_add_item_to_cart(driver):
    """
    Regression Test 1
    Verify item can be added to cart
    """

    logger.info("Starting test: test_add_item_to_cart")

    logger.info("Opening application URL")
    driver.get(config["base_url"])

    logger.info("Logging into application")
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])

    logger.info("Adding backpack item to cart")
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    logger.info("Verifying item count in cart")
    assert "1" in driver.page_source

    logger.info("Test test_add_item_to_cart completed successfully")


@pytest.mark.regression
def test_remove_item_from_cart(driver):
    """
    Regression Test 2
    Verify item can be removed from cart
    """

    logger.info("Starting test: test_remove_item_from_cart")

    logger.info("Opening application URL")
    driver.get(config["base_url"])

    logger.info("Logging into application")
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])

    logger.info("Adding backpack item to cart")
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    logger.info("Navigating to cart page")
    products_page.go_to_cart()

    logger.info("Removing item from cart")
    cart_page = CartPage(driver)
    cart_page.remove_backpack()

    logger.info("Verifying item removed from cart")
    assert "Remove" not in driver.page_source

    logger.info("Test test_remove_item_from_cart completed successfully")