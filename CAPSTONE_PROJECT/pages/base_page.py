from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    
    def __init__(self, driver, timeout = 20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.actions = ActionChains(self.driver)
    
    def load(self,url):
        self.driver.get(url)
        
    def find_web_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_multiple_web_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
    
    def click_operation(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(element).perform()
    
    def context_click_opeartion(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.context_click(element).perform()
    
    def double_click_operation(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.double_click(button).perform()
    
    def presence_of_element(self, locator):
        button = self.wait.until(EC.presence_of_element_located(locator))
        self.actions.click(button).perform()
    
    def alert_function(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


    def scroll_by(self, x=0, y=100):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
    
    def scrollTo_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  
    
    def scroll_into_view(self, locator):
        elem = self.find_web_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        return elem
    def invisibility_of_element(self,locator):
        self.wait.until(EC.invisibility_of_element_located(locator))