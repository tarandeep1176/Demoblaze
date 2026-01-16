from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Logout import LogoutPageObjects
import time

class LogoutPageFunctions(LogoutPageObjects):
    
    def __init__(self, driver):
        self.driver = driver

    def logout_user(self):
        self.driver.find_element(*self.logout_btn).click()
        print("User logged out!")
