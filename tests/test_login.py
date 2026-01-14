from selenium import webdriver
from pages.login_page import LoginPage
from config.config import Config

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Config.BASE_URL)

login = LoginPage(driver)
login.open_login()
login.invalid_case("tarandeep.1176@zenmonk.tech","Taran123@")
login.user_not_exist_case("tarandeeppp.1176@zenmonk.tech","taran123@")
login.valid_case("tarandeep.1176@zenmonk.tech","taran123@")