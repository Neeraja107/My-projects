from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProfileModule(BasePage):
    PROFILE_EDIT_LOCATOR = (By.ID,'ui-id-5')
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
    UPDATE_USER_LOCATOR = (By.NAME,'commit')
    TEXT = (By.XPATH,'//*[@id="tabs-5"]/h1')

    def goto_profile_editor(self,title,fname,surname,phone,year,month,day,licence,occupation,street,city,county,postalcode):
        self.click_operation(self.PROFILE_EDIT_LOCATOR)
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
    
    def update(self):
        self.click_operation(self.UPDATE_USER_LOCATOR)
    def verify_page(self):
        return self.find_web_element(self.TEXT).text
    
    def profile_editor_missing(self,title,fname,surname,phone,year,month,day,licence,occupation,street):
        self.click_operation(self.PROFILE_EDIT_LOCATOR)
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
        