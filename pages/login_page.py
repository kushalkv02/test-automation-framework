from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "button[type='submit']"
    MESSAGE = "#flash"

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_message(self):
        return self.get_text(self.MESSAGE)