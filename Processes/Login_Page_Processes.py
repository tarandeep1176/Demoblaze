from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Data.Login_Page_Data import LoginPageMother

class LoginPageProcess:

    def __init__(self, login:LoginPageFunctions):
        self.login = login

    def run_process(self):
        data = LoginPageMother()
        self.login.open_login()
        self.login.enter_username(data.app_username)
        self.login.enter_password(data.app_password)
        self.login.click_login()
        self.login.verify_login()
