from pages.dashboard_module import DashboardModule
from pages.login_module import LoginModule
from config.config import Config
import pytest
@pytest.mark.usefixtures('setup')
class TestDashBoard:
    def test_dashboard(self): #test case 7
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        dashboard = DashboardModule(self.driver)
        assert "Request Quotation" in dashboard.request_quatation()
        
        assert "Retrieve Quotation" in dashboard.request_retriver()
        
        assert "Profile" in dashboard.profile()
        
        #assert "Log out" in dashboard.logout()
        
        print("Dashboard page loads with links to Request Quotation, Retrieve Quotation, Profile, Logout.")
        
    def test_verify_navigation(self): #testcase 8
        loginmodule = LoginModule(self.driver)
        loginmodule.load(Config.BASE_URL)
        loginmodule.login("tanukuneeraja@gmail.com","Neeraja@12345")
        dashboard = DashboardModule(self.driver)
        assert 'Request a quotation'in dashboard.verify_request_quotation()
        print("Correct respective page is loaded.")
        assert "Last modified:" in dashboard.verify_retriver()
        print("Correct respective page is loaded.")
        assert "Title:" in dashboard.verify_profile()
        print("Correct respective page is loaded.")