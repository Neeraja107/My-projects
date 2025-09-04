from pages.login_module import LoginModule
from config.config import Config
import pytest
@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login(self):
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)#test case 4
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        loginmodule.verify_text()
        loginmodule.load(Config.BASE_URL)#test case 5
        loginmodule.login("tanukuneeraja@gmail.com",'neeraja')
        loginmodule.verify_text2()
    def test_login_with_missing(self):
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login_with_missind_data()
        loginmodule.verify_text()
        print("It has issue that the user can login with blank credentials")# test case 6
