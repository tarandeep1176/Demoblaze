from Page_Functions.Cart_Page_Functions import CartPageFunctions

class CartPageProcess:

    def __init__(self, driver):
        self.cart = CartPageFunctions(driver)

    def place_order(self):
        self.cart.place_order()
        self.cart.get_order_details()

