from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Login_Page import LoginPageObjects
import time


class LoginPageFunctions(LoginPageObjects):
   
        def __init__(self,driver):
                self.driver = driver
                self.wait = WebDriverWait(driver, 15)

        def open_login(self):
                time.sleep(3)  
                self.driver.find_element(*self.login_btn).click()  
                self.wait.until(EC.visibility_of_element_located(self.login_username))
                time.sleep(2)  

        def enter_username(self,username):
                self.open_login()
                time.sleep(1)
                self.wait.until(EC.visibility_of_element_located(self.login_username))
                self.driver.find_element(*self.login_username).send_keys(username)

        def enter_password(self,password):
                self.driver.find_element(*self.login_password).send_keys(password)
                

        def click_login(self):
                self.driver.find_element(*self.submit).click()
                time.sleep(1)

        def verify_login(self):
                welcome_text = self.wait.until(EC.visibility_of_element_located(self.welcome_text))
                if(welcome_text):
                        print("Login successful! - ",welcome_text.text)
