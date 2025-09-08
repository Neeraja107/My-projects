from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_operation(self,locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    def wait_alert(self):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept() 
            print("Alert accepted")
        except TimeoutException:
         print("No alert appeared")
    