from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.take_screenshot import Screenshot
class RetriveModule(BasePage,Screenshot):
    RETRIVE_QUOTATION_LOCATOR = (By.ID,'ui-id-3')
    IDENTIFICATION_NUM = (By.NAME,'id')
    RETRIVE_LOCATOR=(By.ID,'getquote')
    RETRIVE_QUATATION_TEXT = (By.XPATH,'/html/body/b/font')#Retrieve Quotation
    WRONG_RETRIVE_ID_TEXT = (By.XPATH,'/html/body/b')#Wrong Retrieve Quotation ID. Please Check...
    def retrive_quotarton(self,number):
        self.click_operation(self.RETRIVE_QUOTATION_LOCATOR)
        self.enter_text(self.IDENTIFICATION_NUM,number)
        self.click_operation(self.RETRIVE_LOCATOR)

    def verify_retrive_text(self):
        return self.find_web_element(self.RETRIVE_QUATATION_TEXT).text
    
    def verify_wrong_quotation_id(self):
        return self.find_web_element(self.WRONG_RETRIVE_ID_TEXT).text
    
    def empty_quortaion(self):
        self.click_operation(self.RETRIVE_QUOTATION_LOCATOR)
        self.take_screenshot("screenshots/Quortatiion_id_error")
        self.click_operation(self.RETRIVE_LOCATOR)
        self.take_screenshot("screenshots/Quortatiion_id_error")
        print("Redirecting to homepage but not showing Quotation ID is required")
    
    
