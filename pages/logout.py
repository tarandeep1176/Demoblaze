from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Logout:
    def __init__(self, driver):
        self.driver = driver

    def logout_user(self):
        self.driver.find_element(By.ID,"logout2").click()
        print("User logged out!")
