from pages.register_page import RegisterClass
from config.config import Config
from utils.take_screenshot import Screenshot

import pytest
@pytest.mark.usefixtures('setup')
class TestRegister:
    def test_register_module(self): #test case1
        register = RegisterClass(self.driver)
        register.load(Config.BASE_URL)
        register.successfulregistration("Mrs","Neeraja",'Tanuku','6304584832','1947','December','11','5','Teacher','Peravali Road','Tanuku',"India",'534211','tanukuneeraja@gmail.com',"Neeraja@12345",'Neeraja@12345')

    def test_register_with_missing_fields(self):#testcase 2
        register = RegisterClass(self.driver)
        register.load(Config.BASE_URL)
        register.registratiion_with_missing_field()
    
    def test_register_with_invalid_email(self):#test case 3
        register = RegisterClass(self.driver)
        register.load(Config.BASE_URL)
        ss = Screenshot(self.driver)
        ss.take_screenshot("screenshots/registration_errors")
        register.successfulregistration("Mrs","Neeraja",'Tanuku','6304584832','1947','December','11','5','Teacher','Peravali Road','Tanuku',"India",'534211','abc@xyz',"Neeraja@12345",'Neeraja@12345')
        ss.take_screenshot("screenshots/registration_errors")
        print("The page is working with invalid email")

