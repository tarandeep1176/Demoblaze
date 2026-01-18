from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
APP_USERNAME = os.getenv("APP_USERNAME")
APP_PASSWORD = os.getenv("APP_PASSWORD")
from Page_Functions.Signup_Page_Functions import SignupPageFunctions
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.Home_Page_Functions import HomePageFunctions
from Page_Functions.Cart_Page_Functions import CartPageFunctions
from Page_Functions.Logout_Page_Functions import LogoutPageFunctions


from Processes.Signup_Page_Processes import SignupPageProcess
from Processes.Login_Page_Processes import LoginPageProcess
from Processes.Home_Page_Processes import HomePageProcess
from Processes.Cart_Page_Processes import CartPageProcess
from Processes.Logout_Page_Processes import LogoutPageProcess

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BASE_URL)

# signup_page = SignupPageFunctions(driver)
# login_page = LoginPageFunctions(driver)
# home_page = HomePageFunctions(driver)
# cart_page = CartPageFunctions(driver)
# logout_page = LogoutPageFunctions(driver)

def test_signup():
    signup = SignupPageProcess(driver)
    signup.run_process(APP_USERNAME, APP_PASSWORD)

def test_login():
    login = LoginPageProcess(driver)
    login.run_process(APP_USERNAME, APP_PASSWORD)
def test_home():
    home = HomePageProcess(driver)
    home.run_process()

def test_cart():
    cart = CartPageProcess(driver)
    cart.run_process()

def test_logout():
    logout = LogoutPageProcess(driver)
    logout.run_process()