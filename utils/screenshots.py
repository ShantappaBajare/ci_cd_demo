import os
from datetime import datetime

def take_screenshot(driver, name):

    folder = "reports/screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(path)

    return path