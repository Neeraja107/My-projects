from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class DashboardModule(BasePage):
    REQUEST_QUATATION_LOCATOR = (By.LINK_TEXT, "Request Quotation")#Request Quotation
    REQUEST_RETRIVER_LOCATOR = (By.LINK_TEXT, "Retrieve Quotation")#Retrieve Quotation
    PROFILE_LOCATOR = (By.LINK_TEXT, "Profile")#Profile
    LOGOUT_LOCATOR = (By.XPATH, "/html/body/div[3]/form")#Log out
    QUOTATION_TEXT = (By.XPATH,'//*[@id="tabs-2"]/h2')
    RETRIVE_TEXT = (By.XPATH,'//*[@id="tabs"]')
    PROFILE_TEXT = (By.XPATH,'//*[@id="tabs-4"]/p[1]/strong')

    def request_quatation(self):
        return self.find_web_element(self.REQUEST_QUATATION_LOCATOR).text
    def request_retriver(self):
        return self.find_web_element(self.REQUEST_RETRIVER_LOCATOR).text
    def profile(self):
        return self.find_web_element(self.PROFILE_LOCATOR).text
    '''def logout(self):
        return self.find_web_element(self.LOGOUT_LOCATOR).text'''
    def verify_request_quotation(self):
        self.click_operation(self.REQUEST_QUATATION_LOCATOR)
        sleep(2)
        return self.find_web_element(self.QUOTATION_TEXT).text
    def verify_retriver(self):
        self.click_operation(self.REQUEST_RETRIVER_LOCATOR)
        sleep(2)
        return self.find_web_element(self.RETRIVE_TEXT).text
    def verify_profile(self):
        self.click_operation(self.PROFILE_LOCATOR)
        return self.find_web_element(self.PROFILE_TEXT).text

