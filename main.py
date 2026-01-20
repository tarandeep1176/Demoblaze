from Libraries.Libraries import Import_libraries
from Data.Config_Data import ConfigData
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

data = ConfigData()
driver = Import_libraries.initialize_driver()
driver.get(data.BASE_URL)

signup_page_functions = SignupPageFunctions(driver)
login_page_functions = LoginPageFunctions(driver)
home_page_functions = HomePageFunctions(driver)
cart_page_functions = CartPageFunctions(driver)
logout_page_functions = LogoutPageFunctions(driver)

def test_signup():
    signup = SignupPageProcess(signup_page_functions)
    signup.run_process()

def test_login():
    login = LoginPageProcess(login_page_functions)
    login.run_process()

def test_home():
    home = HomePageProcess(home_page_functions)
    home.run_process()

def test_cart():
    cart = CartPageProcess(cart_page_functions)
    cart.run_process()

def test_logout():
    logout = LogoutPageProcess(logout_page_functions)
    logout.run_process()