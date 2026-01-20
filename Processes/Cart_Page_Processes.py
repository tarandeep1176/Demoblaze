from Page_Functions.Cart_Page_Functions import CartPageFunctions

class CartPageProcess:

    def __init__(self, cart:CartPageFunctions):
        self.cart = cart

    def run_process(self):
        self.cart.place_order()
        self.cart.get_order_details()

