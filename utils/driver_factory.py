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

def create_driver():
    options = webdriver.ChromeOptions()

    # ---------------- Local + CI options ----------------
    # Start maximized only for local GUI
    if os.environ.get("CI") != "true":
        options.add_argument("--start-maximized")
    else:
        # Headless mode for CI / Docker
        options.add_argument("--headless=new")          # new headless mode
        options.add_argument("--no-sandbox")            # required in Docker
        options.add_argument("--disable-dev-shm-usage") # prevents /dev/shm crashes
        options.add_argument("--window-size=1920,1080") # ensures proper layout for screenshots

    # ---------------- Notifications & Password ----------------
    options.add_argument("--disable-notifications")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    # ---------------- Extra stability ----------------
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")  # optional, works well in CI

    # ---------------- Create driver ----------------
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    return driver