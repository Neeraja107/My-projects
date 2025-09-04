from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.take_screenshot import Screenshot
class LoginModule(BasePage,Screenshot):
    EMAIL_ID = (By.ID,'email')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.NAME,'submit')
    TEXT_LOCATOR = (By.XPATH,'//*[@id="tabs-1"]/h2')
    TEXT_LOCATOR2 = (By.XPATH,'//*[@id="login-form"]/div[2]/span/b')

    def login(self,mail,passowrd):
        self.enter_text(self.EMAIL_ID,mail)
        self.enter_text(self.PASSWORD,passowrd)
        self.click_operation(self.LOGIN_BUTTON)
    def verify_text(self):
        text = self.find_web_element(self.TEXT_LOCATOR).text
        assert "Broker Insurance WebPage" in text
        print(text)
    def verify_text2(self):
        text1 = self.find_web_element(self.TEXT_LOCATOR2).text
        assert "Enter your Email address and password correct" in text1
        print(text1)
    def login_with_missind_data(self):
        self.take_screenshot("screenshots/login_error")
        self.click_operation(self.LOGIN_BUTTON)
        self.take_screenshot("screenshots/login_error")

