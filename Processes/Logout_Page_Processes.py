from Page_Functions.Logout_Page_Functions import LogoutPageFunctions

class LogoutPageProcess:

    def __init__(self, logout: LogoutPageFunctions):
        self.logout = logout

    def run_process(self):
        self.logout.logout_user()