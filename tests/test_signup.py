from selenium import webdriver
from pages.signup_page import SignupPage
from config.config import Config

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Config.BASE_URL)

signup = SignupPage(driver)
signup.open_signup()
signup.valid_case(Config.APP_USERNAME,Config.APP_PASSWORD)
signup.already_exists_case(Config.APP_USERNAME,Config.APP_PASSWORD)