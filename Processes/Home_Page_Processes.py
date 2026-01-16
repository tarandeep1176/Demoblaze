from Page_Functions.Home_Page_Functions import HomePageFunctions

class HomePageProcess:

    def __init__(self, driver):
        self.home = HomePageFunctions(driver)

    def product_add_to_cart(self):
        self.home.add_to_cart()
        self.home.open_cart_page()

