from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        self.click(self.add_to_cart_backpack)

    def go_to_cart(self):
        self.click(self.cart_icon)