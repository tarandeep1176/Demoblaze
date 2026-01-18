from Page_Functions.Signup_Page_Functions import SignupPageFunctions

class SignupPageProcess:

    def __init__(self, driver):
        self.signup = SignupPageFunctions(driver)

    def run_process(self, username, password):
        self.signup.open_signup()
        self.signup.enter_username(username)
        self.signup.enter_password(password)
        self.signup.click_signup()
        self.signup.accept_signup_alert()

