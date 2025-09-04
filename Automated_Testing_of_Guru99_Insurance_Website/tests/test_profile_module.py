from pages.profile_module import ProfileModule
from pages.login_module import LoginModule
from config.config import Config
from utils.take_screenshot import Screenshot
from time import sleep
import pytest
@pytest.mark.usefixtures('setup')
class TestProfileModule: 
    def test_update_with_validate_data(self):#tesstcase 15
        logiin_obj = LoginModule(self.driver)
        logiin_obj.load(Config.BASE_URL)
        logiin_obj.login("tanukuneeraja@gmail.com","Neeraja@12345")
        profile_obj = ProfileModule(self.driver)
        profile_obj.goto_profile_editor("Mrs","Neeraja",'Tanuku','6304584832','1947','December','11','5','Teacher','Peravali Road','Tanuku',"India",'534211')
        ss=Screenshot(self.driver)
        ss.take_screenshot("screenshots/Edit_profile_errors")
        profile_obj.update()
        ss.take_screenshot("screenshots/Edit_profile_errors")
        assert "Editing user profile" in profile_obj.verify_page()
        print("still in same page the update button is not able to click")

    def test_update_with_missing_data(self): #testcase 16
        logiin_obj = LoginModule(self.driver)
        logiin_obj.load(Config.BASE_URL)
        logiin_obj.login("tanukuneeraja@gmail.com","Neeraja@12345")
        profile_obj = ProfileModule(self.driver)
        profile_obj.profile_editor_missing("Mrs","Neeraja",'Tanuku','6304584832','1947','December','11','5','Teacher','Peravali Road','Tanuku',"India",'534211')
        ss=Screenshot(self.driver)
        ss.take_screenshot("screenshots/Edit_profile_errors")
        profile_obj.update()
        ss.take_screenshot("screenshots/Edit_profile_errors")
        assert "Editing user profile" in profile_obj.verify_page()
        print("still in same page the update button is not able to click")
    
