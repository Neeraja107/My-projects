from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.take_screenshot import Screenshot
class LogoutModule(BasePage):
    LOGOUT_LOCATOR =(By.XPATH,'/html/body/div[3]/form/input')
    LOGIN_TEXT = (By.XPATH,'/html/body/div[3]/h3')

    def logout(self):
        self.click_operation(self.LOGOUT_LOCATOR)
        return self.find_web_element(self.LOGIN_TEXT).text