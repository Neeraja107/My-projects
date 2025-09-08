from pages.make_an_appointment_page import MakeAnAppointment
from config.config import ConfigClass
from utils.take_screenshot import Screenshot
import pytest

@pytest.mark.usefixtures("init_driver")
class TestAppointment:
    def test_appointment(self):
        obj = MakeAnAppointment(self.driver)
        obj.load(ConfigClass.URL)
        obj.performing_operations("John Doe", "ThisIsNotAPassword",23,"December",2025,"no comments at", "Hongkong CURA Healthcare Center")
        
        