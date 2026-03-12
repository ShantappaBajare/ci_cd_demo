import pytest
from pages.login_page import LoginPage
from utils.config_reader import read_config

config = read_config()


@pytest.mark.smoke
def test_valid_login(driver, logger):
    """
    Smoke Test 1
    Verify user can log in with valid credentials
    """

    logger.info(f"Navigating to base URL: {config['base_url']}")
    driver.get(config["base_url"])

    login_page = LoginPage(driver)
    logger.info(f"Logging in with valid username: {config['username']}")
    login_page.login(config["username"], config["password"])

    current_url = driver.current_url
    logger.info(f"Current URL after login: {current_url}")

    assert "inventory" in current_url
    logger.info("Valid login test passed ✅")


@pytest.mark.smoke
def test_invalid_login(driver, logger):
    """
    Smoke Test 2
    Verify error message appears for invalid credentials
    """

    logger.info(f"Navigating to base URL: {config['base_url']}")
    driver.get(config["base_url"])

    login_page = LoginPage(driver)
    logger.info("Attempting login with invalid credentials")
    login_page.login("wrong_user", "wrong_password")

    error = login_page.get_error_message()
    logger.info(f"Error message received: {error}")

    assert "Username and password do not match" in error
    logger.info("Invalid login test passed ✅")