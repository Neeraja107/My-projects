from selenium.webdriver.common.by import By
from utils.util import BaseUtil
from utils.take_screenshot import Screenshot
from time import sleep

class MakeAnAppointment(BaseUtil,Screenshot):
    MAKE_APPOINTEMENT_BUTTON_LOCATOR = (By.ID, "btn-make-appointment")
    USER_NAME_LOCATOR = (By.ID, "txt-username")
    USER_PASSWORD_LOCATOR = (By.ID, "txt-password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "btn-login")
    SELECTOR_ID_LOCATOR = (By.ID, "combo_facility")
   # SELECT_OPTION_LOCATOR = (By.XPATH, '//option[@value="Tokyo CURA Healthcare Center"]')
    CHECKBOX_LOCATOR = (By.NAME, "hospital_readmission")
    HEALTH_PROGRAM_CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="appointment"]/div/div/form/div[3]/div/label[2]')
    DATE_LOCATOR = (By.NAME, "visit_date")
    CALENDER_HEADER = (By.CLASS_NAME, "datepicker-switch")
    NEXT_BUTTON = (By.XPATH, "//th[@class='next']")
    PREV_BUTTON = (By.XPATH, "//th[@class='prev']")
    CALENDAR_DAYS = (By.XPATH, "//td[@class='day']")
    COMMENT_BOX_LOCATOR = (By.NAME, "comment")
    BOOK_BUTTON_LOCATOR = (By.ID, "btn-book-appointment")
    CONFIRMATION_HEADER = (By.TAG_NAME, "h2")
    HOME_PAGE_LOCATOR = (By.XPATH, '//*[@id="summary"]/div/div/div[7]/p/a')
    MENU_BUTTON_LOCATOR = (By.ID, "menu-toggle")
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[5]/a')


    def performing_operations(self,username,password,day,month,year,comments,text):
        self.wait_for_click(self.MAKE_APPOINTEMENT_BUTTON_LOCATOR)
        sleep(2)
        self.wait_for_enter_text(self.USER_NAME_LOCATOR,username)
        sleep(2)
        self.wait_for_enter_text(self.USER_PASSWORD_LOCATOR,password)
        sleep(2)
        self.wait_for_click(self.LOGIN_BUTTON_LOCATOR)
        sleep(2)
        self.wait_for_dropdown(self.SELECTOR_ID_LOCATOR,text)
        sleep(2)
        self.wait_for_click(self.CHECKBOX_LOCATOR)
        sleep(2)
        self.wait_for_click(self.HEALTH_PROGRAM_CHECKBOX_LOCATOR)
        sleep(2)
        self.wait_for_click(self.DATE_LOCATOR)
        sleep(2)
        self.wait_for_visible(self.CALENDER_HEADER)
        while True:
            header = self.wait_for_visible(self.CALENDER_HEADER).text
            if f"{month} {year}" in header:
                break
            self.wait_for_click(self.NEXT_BUTTON)
            slice(0.2)

        all_days = self.driver.find_elements(*self.CALENDAR_DAYS)
        for d in all_days:
            if d.text == str(day):
                d.click()
                break

        sleep(2)
        self.wait_for_enter_text(self.COMMENT_BOX_LOCATOR,comments)
        sleep(2)
        self.wait_for_click(self.BOOK_BUTTON_LOCATOR)
        sleep(2)
        self.wait_for_visible(self.CONFIRMATION_HEADER)
        sleep(2)
        self.take_screenshot("screenshots/appointment")
        self.wait_for_click(self.HOME_PAGE_LOCATOR)
        sleep(2)
        self.wait_for_click(self.MENU_BUTTON_LOCATOR)
        sleep(2)
        self.wait_for_click(self.LOGOUT_BUTTON_LOCATOR)
        sleep(5)