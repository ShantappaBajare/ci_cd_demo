from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    success_message = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, first, last, postal):
        self.send_keys(self.first_name, first)
        self.send_keys(self.last_name, last)
        self.send_keys(self.postal_code, postal)
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def get_success_message(self):
        return self.get_text(self.success_message)