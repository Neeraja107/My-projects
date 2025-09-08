from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BaseUtil:

    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.action = ActionChains(driver)

        
    def load(self,url):
        self.driver.get(url)

    def wait_for_visible(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator))


    def wait_for_click(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_for_presence(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(locator))

    def wait_for_enter_text(self,locator,text):
        WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_url_contains(self,url_fragment):
        return WebDriverWait(self.driver,self.timeout).until(EC.url_contains(url_fragment))
    
    def wait_for_double_click(self,locator):
        double = self.wait_for_visible(locator)
        self.action.double_click(double).perform()
    
    def wait_for_right_click(self,locator):
        right = self.wait_for_visible(locator)
        self.action.context_click(right).perform()
    
    def wait_for_dropdown (self,locator,text):
        dropdown = self.wait_for_visible(locator)
        select = Select(dropdown)
        select.select_by_visible_text(text)
    

    
    