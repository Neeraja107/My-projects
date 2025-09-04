from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.take_screenshot import Screenshot

class RegisterClass(BasePage,Screenshot):
    REGISTER_BUTTON = (By.XPATH,'/html/body/div[3]/a')
    TITLE_LOCATOR = (By.ID,'user_title')
    FIRSTNAME_LOCATOR = (By.ID,'user_firstname')
    SURNAME_LOCATOR =(By.ID,'user_surname')
    PHONE_LOCATOR = (By.ID,'user_phone')
    YEAR_LOCATOR = (By.ID,'user_dateofbirth_1i')
    MONTH_LOCATOR = (By.ID,'user_dateofbirth_2i')
    DAY_LOCATOR = (By.ID,'user_dateofbirth_3i')
    PROFESSIONAL_LOCATOR = (By.ID,'licencetype_f')
    LICENCE_LOCATOR = (By.ID,'user_licenceperiod')
    OCCUPATION_LOCATOR = (By.ID,'user_occupation_id')
    STREET_LOCATOR = (By.ID,'user_address_attributes_street')
    CITY_LOCATOR = (By.ID,'user_address_attributes_city')
    COUNTY_LOCATOR = (By.ID,'user_address_attributes_county')
    POSTAL_CODE = (By.ID,'user_address_attributes_postcode')
    EMAIL_LOCATOR = (By.ID,'user_user_detail_attributes_email')
    PASSWORD_LOCATOR = (By.ID,'user_user_detail_attributes_password')
    CONFIRM_PASSWORD = (By.ID,'user_user_detail_attributes_password_confirmation')
    CREATE_BUTTON = (By.NAME,'submit')
    LOGIN_TEXT = (By.XPATH,'/html/body/div[3]/h3')

    def successfulregistration(self,title,fname,surname,phone,year,month,day,licence,occupation,street,city,county,postalcode,email,password,cpassword):
        self.click_operation(self.REGISTER_BUTTON)
        Select(self.find_web_element(self.TITLE_LOCATOR)).select_by_visible_text(title)
        self.enter_text(self.FIRSTNAME_LOCATOR,fname)
        self.enter_text(self.SURNAME_LOCATOR,surname)
        self.enter_text(self.PHONE_LOCATOR,phone)
        Select(self.find_web_element(self.YEAR_LOCATOR)).select_by_visible_text(year)
        Select(self.find_web_element(self.MONTH_LOCATOR)).select_by_visible_text(month)
        Select(self.find_web_element(self.DAY_LOCATOR)).select_by_visible_text(day)
        self.click_operation(self.PROFESSIONAL_LOCATOR)
        Select(self.find_web_element(self.LICENCE_LOCATOR)).select_by_visible_text(licence)
        Select(self.find_web_element(self.OCCUPATION_LOCATOR)).select_by_visible_text(occupation)
        self.enter_text(self.STREET_LOCATOR,street)
        self.enter_text(self.CITY_LOCATOR,city)
        self.enter_text(self.COUNTY_LOCATOR,county)
        self.enter_text(self.POSTAL_CODE,postalcode)
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.enter_text(self.PASSWORD_LOCATOR,password)
        self.enter_text(self.CONFIRM_PASSWORD,cpassword)
        self.click_operation(self.CREATE_BUTTON)
        print("Account is created successfully.")
        text = self.find_web_element(self.LOGIN_TEXT).text
        assert "Login" in text

    def registratiion_with_missing_field(self):
        self.click_operation(self.REGISTER_BUTTON)
        self.take_screenshot("screenshots/registration_errors")
        self.click_operation(self.CREATE_BUTTON)
        self.take_screenshot("screenshots/registration_errors")
        text = self.find_web_element(self.LOGIN_TEXT).text
        assert "Login" in text
        print("It has an error it creating a new account with missing fields")




        

