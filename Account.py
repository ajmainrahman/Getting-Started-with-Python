class Account:
    def __init__(self,billingAddress, delivaryAddress, emailAddress, name):
        self.billingAddress = billingAddress
        self.delivaryAddress = delivaryAddress
        self.emailAddress = emailAddress
        self.name = name
        self.closed = False
        self.orders = []
    def createnewaccount(self):
        print("New Account Created")
    def loadaccountdeatils(self):
        print("Account Details loaded")
    def markaccountclosed(self):
        print("Account marked as closed")
    def retrieveaccountdetails(self):
        print("New Account details retrieved")
    def submitnewaccountdetails(self):
        print("New Account details submitted")
    def validation(self,username,password):
        if username =='admin' and password == 'password':
            return True
        else:
            return False
class Order:
    def __init__(self, date, delivery_instruction, order_number):
        self._date = date
        self._delivery_instruction = delivery_instruction
        self._order_number = order_number
        self.trasactions = []

    def loadaccounthistory(self):
        print("Accout History loaded")
    def loadopenorder(self):
        print("Open order loaded")
    def add_transaction(self, transaction):
        self.trasactions.append(transaction)
        print("Transaction added to the order")

class ShoppingBasket:
    def __init__(self, shoppingbasketnumber, date):
        self.date = date
        self._shoppingbasketnumber = shoppingbasketnumber

    def addlineitem(self):
        print("Line item")

    def createnewbasket(self):
        print("CreateNewBasket")

    def deleteitem(self):
        print("deleteItem")

    def processOrder(self):
        print("ProcessOrder")

class Transaction:
    def __init__(self,date, Ordernumber):
        self._date = date
        self._Ordernumber = Ordernumber
    def loadaccounthistory(self):
        print("Accout History loaded")
    def loadopenorder(self):
        print("Open order loaded")

#create account instance
account = Account(billingAddress="123 Main str",delivaryAddress="456 elm str", emailAddress="abc@gmail.com",name="Mr. Kuddosh")

#Order Instance
order = Order(date="2023-05-12",delivery_instruction="Be careful",order_number="ORD123")

#Shopping instance
shopping = ShoppingBasket(date="2023-5-12",shoppingbasketnumber="123ABC")

#Transcation instance
transaction = Transaction(date="2023-4-2",Ordernumber="23BNC")

order.add_transaction(transaction)

account_orders = account._Orders
account_orders.append(order)

order_transaction = order.trasactions
order_transaction.append(transaction)
