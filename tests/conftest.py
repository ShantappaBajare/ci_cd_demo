import pytest
from datetime import datetime
import os

from utils.driver_factory import create_driver
from utils.logger import get_logger


# ---------------------------------
# Timestamp for this test execution
# ---------------------------------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


# ---------------------------------
# Base directories
# ---------------------------------
BASE_DIR = os.getcwd()

LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ---------------------------------
# Logger Fixture
# ---------------------------------
@pytest.fixture(scope="session")
def logger():
    log_file = os.path.join(LOG_DIR, f"logs_{timestamp}.log")
    logger = get_logger(log_file)
    return logger


# ---------------------------------
# WebDriver Fixture
# ---------------------------------
@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


# ---------------------------------
# Screenshot on failure
# ---------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver")

        if driver:
            test_name = item.name

            screenshot_file = os.path.join(
                SCREENSHOT_DIR,
                f"{test_name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_file)


# ---------------------------------
# HTML Report path
# ---------------------------------
def pytest_configure(config):

    report_file = os.path.join(
        REPORT_DIR,
        f"report_{timestamp}.html"
    )

    config.option.htmlpath = report_file
    config.option.self_contained_html = True




# import pytest
# from datetime import datetime
# import os
# from utils.driver_factory import create_driver
# from utils.logger import get_logger
#
# # --------------------------
# # Environment Setup
# # --------------------------
# ENV = os.environ.get("ENV", "local")  # local or ci
# IS_CI = ENV.lower() == "ci"
#
# # --------------------------
# # Timestamp per test run
# # --------------------------
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# BASE_RUN_DIR = os.path.join(os.getcwd(), f"TestRun_{timestamp}")
#
# # Create folder structure
# LOG_DIR = os.path.join(BASE_RUN_DIR, "logs")
# SCREENSHOT_DIR = os.path.join(BASE_RUN_DIR, "screenshots")
# REPORT_DIR = os.path.join(BASE_RUN_DIR, "reports")
#
# os.makedirs(LOG_DIR, exist_ok=True)
# os.makedirs(SCREENSHOT_DIR, exist_ok=True)
# os.makedirs(REPORT_DIR, exist_ok=True)
#
# # --------------------------
# # Logger Fixture
# # --------------------------
# @pytest.fixture(scope="session")
# def logger():
#     log_file = os.path.join(LOG_DIR, f"logs_{timestamp}.log")
#     return get_logger(log_file)
#
# # --------------------------
# # WebDriver Fixture
# # --------------------------
# @pytest.fixture(scope="function")
# def driver():
#     driver = create_driver()
#     yield driver
#     driver.quit()
#
# # --------------------------
# # Screenshot on Failure
# # --------------------------
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             test_name = item.name
#             screenshot_file = os.path.join(SCREENSHOT_DIR, f"{test_name}_{timestamp}.png")
#             driver.save_screenshot(screenshot_file)
#
# # --------------------------
# # HTML Report Path
# # --------------------------
# def pytest_sessionstart(session):
#     if session.config.pluginmanager.hasplugin("html"):
#         report_file = os.path.join(REPORT_DIR, f"report_{timestamp}.html")
#         session.config.option.htmlpath = report_file