#breakdown,incidents,registration,milege,value,parkinglocatiion,year,month,day):
from pages.login_module import LoginModule
from pages.request_quotation_module import RequestQuotation
from config.config import Config
from utils.take_screenshot import Screenshot
import pytest
@pytest.mark.usefixtures('setup')
class TestRequestQuotation:
    def test_request_withvalid(self): #testcase 9
        logiin_obj = LoginModule(self.driver)
        logiin_obj.load(Config.BASE_URL)
        logiin_obj.login("tanukuneeraja@gmail.com","Neeraja@12345")
        request_obj = RequestQuotation(self.driver)
        request_obj.goto_request_quotation('At home','No previous incidents','N12E34','12000','40000','Public Place','2014','December','16')
        assert 'You have saved this quotation!' in request_obj.verify_quotation()
        print('You have saved this quotation!')
        assert "Your identification number is" in request_obj.verify_Identification()
        print("Your identification number is visible")
        
    def test_missing_filed(self): #testcase 10
        logiin_obj = LoginModule(self.driver)
        logiin_obj.load(Config.BASE_URL)
        logiin_obj.login("tanukuneeraja@gmail.com","Neeraja@12345")
        request_obj = RequestQuotation(self.driver)
        request_obj.missing_fields()
        assert 'You have saved this quotation!' in request_obj.verify_quotation()
        print("Working with invalid credentials")

        
    def test_with_invalid_data(self):#test case 11
        logiin_obj = LoginModule(self.driver)
        logiin_obj.load(Config.BASE_URL)
        logiin_obj.login("tanukuneeraja@gmail.com","Neeraja@12345")
        request_obj = RequestQuotation(self.driver)
        request_obj.invalid_details('At home','No previous incidents','N12E34','dkfj','jkk','Public Place','2014','December','16')
        assert 'You have saved this quotation!' in request_obj.verify_quotation()
        print('added wrong details still shows You have saved this quotation!')
        assert "Your identification number is" in request_obj.verify_Identification()
        print("added wrong details still it showsYour identification number is visible")
        

 
