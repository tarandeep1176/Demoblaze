from selenium import webdriver
from pages.home_page import HomePage
from config.config import Config

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Config.BASE_URL)

home = HomePage(driver)
home.add_to_cart()
home.open_cart_page()