from pages.retrive_quotation_module import RetriveModule
from pages.login_module import LoginModule
from config.config import Config
from time import sleep
import pytest
@pytest.mark.usefixtures('setup')
class TestRetriveQuotation:
    def test_retrive_quotation(self): #testcase 12
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        retrive_obj= RetriveModule(self.driver)
        retrive_obj.retrive_quotarton("12345")
        assert 'Retrieve Quotation' in retrive_obj.verify_retrive_text()
        print("Quotation details are displayed")

    def test_wrong_quotation_error(self): #test case 13
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        retrive_obj= RetriveModule(self.driver)
        retrive_obj.retrive_quotarton("123456")
        assert "Wrong Retrieve Quotation ID. Please Check." in retrive_obj.verify_wrong_quotation_id()
        sleep(1)
        print('Wrong Retrieve Quotation ID. Please Check.')

    def test_empty_quotation_error(self):#test case 14
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        retrive_obj= RetriveModule(self.driver)
        retrive_obj.empty_quortaion()

