from pages.logout_module import LogoutModule
from pages.login_module import LoginModule
from config.config import Config
from time import sleep
import pytest
@pytest.mark.usefixtures('setup')
class TestLogout:
    def test_logout(self):
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        logout_obj = LogoutModule(self.driver)
        assert "Login" in logout_obj.logout()
        sleep(1)
        print('User is redirected to login page.')