import pytest
from utils.broswer_factory import get_browser
from config.config import Config

@pytest.fixture(scope="class")
def setup(request):
    driver = get_browser('chrome')
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    yield
    print("All test cases passed!")
    driver.quit()
