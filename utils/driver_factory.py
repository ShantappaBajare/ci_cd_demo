# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# def create_driver():
#
#     options = webdriver.ChromeOptions()
#
#     options.add_argument("--start-maximized")
#
#     # Disable notifications
#     options.add_argument("--disable-notifications")
#
#     # Disable Chrome password manager completely
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#         "profile.password_manager_leak_detection": False
#     }
#
#     options.add_experimental_option("prefs", prefs)
#
#     # Extra stability flags
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-popup-blocking")
#
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )
#
#     driver.implicitly_wait(10)
#
#     return driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

ENV = os.environ.get("ENV", "local")
IS_CI = ENV.lower() == "ci"


def create_driver():
    options = webdriver.ChromeOptions()

    if IS_CI:
        # CI / Docker safe flags
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        # Local flags
        options.add_argument("--start-maximized")

    # Common flags
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    return driver