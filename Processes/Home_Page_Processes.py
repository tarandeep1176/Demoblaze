from Page_Functions.Home_Page_Functions import HomePageFunctions

class HomePageProcess:

    def __init__(self, home:HomePageFunctions):
        self.home = home

    def run_process(self):
        self.home.add_to_cart()
        self.home.open_cart_page()

