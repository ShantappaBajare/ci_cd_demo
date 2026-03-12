class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find(self, by_locator):
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.find(by_locator).click()

    def send_keys(self, by_locator, text):
        self.find(by_locator).clear()
        self.find(by_locator).send_keys(text)

    def get_text(self, by_locator):
        return self.find(by_locator).text