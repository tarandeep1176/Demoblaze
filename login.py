from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()


def invalid_case():
        driver.get("https://www.demoblaze.com/")
        driver.find_element(By.ID,"login2").click()
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"loginusername")))
        driver.find_element(By.ID,"loginusername").send_keys("tarandeep.1176@zenmonk.tech")
        driver.find_element(By.ID,"loginpassword").send_keys("Taran123@")
        driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()

time.sleep(2)
def user_not_exist_case():
        driver.get("https://www.demoblaze.com/")
        driver.find_element(By.ID,"login2").click()
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"loginusername")))
        driver.find_element(By.ID,"loginusername").send_keys("tarandeeppp.1176@zenmonk.tech")
        driver.find_element(By.ID,"loginpassword").send_keys("taran123@")
        driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()

time.sleep(2)
def valid_case():
        driver.get("https://www.demoblaze.com/")
        driver.find_element(By.ID,"login2").click()
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"loginusername")))
        driver.find_element(By.ID,"loginusername").send_keys("tarandeep.1176@zenmonk.tech")
        driver.find_element(By.ID,"loginpassword").send_keys("taran123@")
        driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
        time.sleep(1)
        welcome_text = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"nameofuser")))
        if(welcome_text):
                print("Login successful! - ",welcome_text.text)

user_not_exist_case()
invalid_case()
valid_case()


driver.close()