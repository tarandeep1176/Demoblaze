from Page_Functions.Logout_Page_Functions import LogoutPageFunctions

class LogoutPageProcess:

    def __init__(self, driver):
        self.logout = LogoutPageFunctions(driver)

    def logout_user(self):
        self.logout.logout_user()