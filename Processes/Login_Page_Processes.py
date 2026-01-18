from Page_Functions.Login_Page_Functions import LoginPageFunctions

class LoginPageProcess:

    def __init__(self, driver):
        self.signup = LoginPageFunctions(driver)

    def run_process(self, username, password):
        self.signup.open_login()
        self.signup.enter_username(username)
        self.signup.enter_password(password)
        self.signup.click_login()
        self.signup.verify_login()

