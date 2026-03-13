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

#passes the environment variable from system env variables
#if not present then "local" will be passed as env parameter
ENV = os.environ.get("ENV", "local")

#in docker file we will pass this variable as ENV ENV=ci
IS_CI = ENV.lower() == "ci"


def create_driver():
    options = webdriver.ChromeOptions()

    if IS_CI:
        # CI / Docker safe flags
        options.add_argument("--headless=new") # to run new headless mode engine faster
        options.add_argument("--no-sandbox") # don't run security check bec browser will crash due to no support
        options.add_argument("--disable-dev-shm-usage") # disable shared mem on lin bec less 64mb
        options.add_argument("--window-size=1920,1080")
    else:
        # Local flags
        options.add_argument("--start-maximized")

    # Common flags
    options.add_argument("--disable-notifications") #Allow notifications
    options.add_argument("--disable-extensions") #google password manager to save or update password
    options.add_argument("--disable-popup-blocking") # download,payment windows blocking
    options.add_argument("--disable-infobars") # cheome is controlled by automated software

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
    driver.implicitly_wait(1)
    return driver