from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout import Logout
from config.config import Config

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Config.BASE_URL)

login = LoginPage(driver)
login.open_login()
login.valid_case("tarandeep.1176@zenmonk.tech", "taran123@")

logout = Logout(driver)
logout.logout_user()
