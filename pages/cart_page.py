from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    checkout_button = (By.ID, "checkout")
    remove_backpack_btn = (By.ID, "remove-sauce-labs-backpack")

    def checkout(self):
        self.click(self.checkout_button)

    def remove_backpack(self):
        self.click(self.remove_backpack_btn)