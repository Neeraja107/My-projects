from selenium import webdriver

def get_broswer(browser):
    if browser.lower() == "chrome":
        return webdriver.Chrome()
    elif browser.lower() == "edge":
        return webdriver.Edge()
    elif browser.lower() == "safari":
        return webdriver.Safari()
    elif browser.lower() == "firefox":
        return webdriver.Firefox()
    
