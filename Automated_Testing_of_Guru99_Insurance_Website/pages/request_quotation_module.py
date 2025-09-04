from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.take_screenshot import Screenshot
from time import sleep
class RequestQuotation(BasePage,Screenshot):
    REQUEST_QUOTATION_LOCATOR = (By.ID,'ui-id-2')
    REQUEST_QUOTATION_TEXT = (By.XPATH,'//*[@id="tabs-2"]/h2')
    BREAKDOWNCOVER = (By.ID,'quotation_breakdowncover')
    WINDOWS_SCREEN=(By.ID,'quotation_windscreenrepair_t')
    INCIDENTS_LOCATOR = (By.ID,'quotation_incidents')
    REGISTRATION_LOCATOR = (By.ID,'quotation_vehicle_attributes_registration')
    VECHILE_MILEGE = (By.ID,'quotation_vehicle_attributes_mileage')
    ESTIMATED_VALUE_LOCATOR = (By.ID,'quotation_vehicle_attributes_value')
    PARKING_LOCATION_LOCATOR = (By.ID,'quotation_vehicle_attributes_parkinglocation')
    POLICY_YEAR = (By.ID,'quotation_vehicle_attributes_policystart_1i')
    POLICY_MONTH = (By.ID,'quotation_vehicle_attributes_policystart_2i')
    POLICY_DAY = (By.ID,'quotation_vehicle_attributes_policystart_3i')
    SAVE_QUOTATION = (By.XPATH,'//*[@id="new_quotation"]/div[8]/input[3]')
    SAVE_QUOTATION_TEXT = (By.XPATH,'/html/body/b[1]')
    IDENTIFICATION_NO = (By.XPATH,'/html/body/b[2]')

    def goto_request_quotation(self,breakdown,incidents,registration,milege,value,parkinglocatiion,year,month,day):
        self.click_operation(self.REQUEST_QUOTATION_LOCATOR)
        Select(self.find_web_element(self.BREAKDOWNCOVER)).select_by_visible_text(breakdown)
        self.click_operation(self.WINDOWS_SCREEN)
        self.enter_text(self.INCIDENTS_LOCATOR,incidents)
        self.enter_text(self.REGISTRATION_LOCATOR,registration)
        self.enter_text(self.VECHILE_MILEGE,milege)
        self.enter_text(self.ESTIMATED_VALUE_LOCATOR,value)
        Select(self.find_web_element(self.PARKING_LOCATION_LOCATOR)).select_by_visible_text(parkinglocatiion)
        Select(self.find_web_element(self.POLICY_YEAR)).select_by_visible_text(year)
        Select(self.find_web_element(self.POLICY_MONTH)).select_by_visible_text(month)
        Select(self.find_web_element(self.POLICY_DAY)).select_by_visible_text(day)
        self.click_operation(self.SAVE_QUOTATION)
    def verify_quotation(self):
        return self.find_web_element(self.SAVE_QUOTATION_TEXT).text
    def verify_Identification(self):
        return self.find_web_element(self.IDENTIFICATION_NO).text
    def missing_fields(self):
        self.click_operation(self.REQUEST_QUOTATION_LOCATOR)
        self.scroll_into_view(self.REQUEST_QUOTATION_TEXT)
        self.take_screenshot("screenshots/quotation_working_without_details")
        self.click_operation(self.SAVE_QUOTATION)
        self.take_screenshot("screenshots/quotation_working_without_details")
        sleep(2)
    def invalid_details(self,breakdown,incidents,registration,milege,value,parkinglocatiion,year,month,day):
        self.click_operation(self.REQUEST_QUOTATION_LOCATOR)
        Select(self.find_web_element(self.BREAKDOWNCOVER)).select_by_visible_text(breakdown)
        self.click_operation(self.WINDOWS_SCREEN)
        self.scroll_into_view(self.REQUEST_QUOTATION_TEXT)
        self.enter_text(self.INCIDENTS_LOCATOR,incidents)
        self.enter_text(self.REGISTRATION_LOCATOR,registration)
        self.enter_text(self.VECHILE_MILEGE,milege)
        self.enter_text(self.ESTIMATED_VALUE_LOCATOR,value)
        Select(self.find_web_element(self.PARKING_LOCATION_LOCATOR)).select_by_visible_text(parkinglocatiion)
        Select(self.find_web_element(self.POLICY_YEAR)).select_by_visible_text(year)
        Select(self.find_web_element(self.POLICY_MONTH)).select_by_visible_text(month)
        Select(self.find_web_element(self.POLICY_DAY)).select_by_visible_text(day)
        self.click_operation(self.SAVE_QUOTATION)