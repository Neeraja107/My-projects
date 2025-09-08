from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from time import sleep
class LoginPage(BasePage):
    USERNAME = (By.ID,'user-name')
    PASSWORD = (By.ID,'password')
    LOGIN = (By.ID,'login-button')
    SWAGLAB_TEXT = (By.CLASS_NAME,'app_logo')
    PRODUCT1 = (By.ID,'add-to-cart-sauce-labs-backpack')
    PRODUCT2 = (By.ID,'add-to-cart-sauce-labs-bike-light')
    PRODUCT3 = (By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
    CLICK_CART = (By.CLASS_NAME,'shopping_cart_link')
    CART_TEXT1 = (By.XPATH,'//*[@id="item_4_title_link"]/div')
    CART_TEXT2 = (By.XPATH,'//*[@id="item_0_title_link"]/div')
    CART_TEXT3 = (By.XPATH,'//*[@id="item_1_title_link"]/div')
    CHECKOUT_BUTTON = (By.ID,'checkout')
    FIRSTNAME = (By.ID,'first-name')
    LASTNAME = (By.ID,'last-name')
    POSTALCODE = (By.ID,'postal-code')
    CONTINUE = (By.ID,'continue')
    CHECKOUT_TEXT = (By.CLASS_NAME,'title')
    FINISH_BUTTON = (By.ID,'finish')
    THANKYOU_TEXT = (By.CLASS_NAME,'complete-header')
    BACK_HOME_BUTTON = (By.ID,'back-to-products')
    MENU_BUTTON = (By.ID,'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID,'logout_sidebar_link')
    LOGOUT_TEXT = (By.CLASS_NAME,'login_logo')

    def login(self, username, password):
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click_operation(self.LOGIN)
       # self.wait_alert()

    def verify_text(self):
        return self.get_text(self.SWAGLAB_TEXT)
    
    def add_to_cart(self):
        self.click_operation(self.PRODUCT1)
        sleep(1)
        self.click_operation(self.PRODUCT2)
        sleep(1)
        self.click_operation(self.PRODUCT3)
        sleep(1)
        self.click_operation(self.CLICK_CART)
        sleep(1)
    
    def verify_cart_product1(self):
        return self.get_text(self.CART_TEXT1)
    
    def verify_cart_product2(self):
        return self.get_text(self.CART_TEXT2)
    
    def verify_cart_product3(self):
        return self.get_text(self.CART_TEXT3)

    def add_checkout_details(self,fname,lname,zipcode):
        self.click_operation(self.CHECKOUT_BUTTON)
        sleep(1)
        self.enter_text(self.FIRSTNAME, fname)
        sleep(1)
        self.enter_text(self.LASTNAME,lname)
        sleep(1)
        self.enter_text(self.POSTALCODE,zipcode)
        sleep(1)
        self.click_operation(self.CONTINUE)

    def verify_checkout(self):
        return self.get_text(self.CHECKOUT_TEXT)
    
    def finish(self):
        sleep(1)
        self.click_operation(self.FINISH_BUTTON)

    def verify_finish(self):
        return self.get_text(self.THANKYOU_TEXT)
    
    def logout_button(self):
        self.click_operation(self.BACK_HOME_BUTTON)
        sleep(1)
        self.click_operation(self.MENU_BUTTON)
        sleep(1)
        self.click_operation(self.LOGOUT_BUTTON)
        sleep(1)

    def verify_logout_text(self):
        return self.get_text(self.LOGOUT_TEXT)