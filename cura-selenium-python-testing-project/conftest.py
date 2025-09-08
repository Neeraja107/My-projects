import pytest
from utils.browser_factory import get_broswer
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    driver = get_broswer("chrome")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()