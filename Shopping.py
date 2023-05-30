class ShoppingBasket:
    def __init__(self,shoppingbasketnumber):
        self._shoppingbasketnumber = shoppingbasketnumber

    def addlineitem(self):
        print("Line item")
    def createnewbasket(self):
        print("CreateNewBasket")
    def deleteitem(self):
        print("deleteItem")
    def processOrder(self):
        print("ProcessOrder")

shop = ShoppingBasket("BASKET12")
shop.addlineitem()
shop.createnewbasket()
shop.deleteitem()
shop.processOrder()