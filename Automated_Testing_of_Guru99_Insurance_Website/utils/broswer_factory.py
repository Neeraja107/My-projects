from selenium import webdriver

def get_browser(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() =='edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"{browser} is not a valid browser")

    # ⬇️ Decrease zoom size (e.g., 50%)
    driver.execute_script("document.body.style.zoom='50%'")

    return driver
