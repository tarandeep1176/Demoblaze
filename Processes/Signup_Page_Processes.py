from Page_Functions.Signup_Page_Functions import SignupPageFunctions
from Data.Signup_Page_Data import SignupPageMother 

class SignupPageProcess:

    def __init__(self, sign_up:SignupPageFunctions):
        self.sign_up = sign_up

    def run_process(self):
        data = SignupPageMother()
        self.sign_up.open_signup()
        self.sign_up.enter_username(data.app_username)
        self.sign_up.enter_password(data.app_password)
        self.sign_up.click_signup()
        self.sign_up.accept_signup_alert()
