class Account:
    def init(self, billing_address, delivery_address, email_address, name):
        self._billing_address = billing_address
        self._closed = False
        self._delivery_address = delivery_address
        self._email_address = email_address
        self._name = name
        self._orders = []

    def create_new_account(self):
        # Perform logic to create a new account
        print("New account created.")

    def load_account_details(self):
        # Load and display the account details
        print("Account details loaded.")

    def mark_account_closed(self):
        self._closed = True
        print("Account marked as closed.")

    def retrieve_account_details(self):
        # Retrieve and display the account details
        print("Account details retrieved.")

    def submit_new_account_details(self):
        # Submit and update the account details
        print("New account details submitted.")

    def validate_user(self, username, password):
        # Perform validation logic to validate the user
        # Return True if the user is valid, False otherwise
        if username == "admin" and password == "password":
            return True
        else:
            return False


class Order:
    def init(self, date, order_number,delivaryinstrucations):
        self._date = date
        self._order_number = order_number
        self._transactions = []

    def load_account_history(self):
        # Load the account history based on the order details
        print("Account history loaded.")

    def load_open_order(self):
        # Load the details of the open order based on the order details
        print("Open order loaded.")

    def add_transaction(self, transaction):
        self._transactions.append(transaction)
        print("Transaction added to the order.")


class ShoppingBasket:
    def init(self, date, shopping_basket_number):
        self._date = date
        self._shopping_basket_number = shopping_basket_number

    def add_line_item(self):
        # Perform logic to add a line item to the shopping basket
        print("Line item added to the shopping basket.")

    def create_new_basket(self):
        # Create a new shopping basket
        print("New shopping basket created.")

    def delete_item(self):
        # Perform logic to delete an item from the shopping basket
        print("Item deleted from the shopping basket.")

    def process_order(self):
        # Process the order from the shopping basket
        print("Order processed.")


class Transaction:
    def init(self, date, order_number):
        self._date = date
        self._order_number = order_number

    def load_account_history(self):
        # Load the account history based on the transaction details
        print("Account history loaded.")

    def load_open_order(self):
        # Load the details of the open order based on the transaction details
        print("Open order loaded.")


# Create instances of the classes and establish connections

# Create an Account instance
account = Account(billing_address = "123 Main St", delivery_address="456 Elm St", email_address="example@example.com", name="John Doe")

# Create an Order instance
order = Order(date="2023-05-28", order_number="ORD123")

# Create a ShoppingBasket instance
shopping_basket = ShoppingBasket(date="2023-05-28", shopping_basket_number="BASKET123")

# Add the Transaction to the Order
order.add_transaction(Transaction)

# Connect the Account with the Order
account_orders = account._orders
account_orders.append(order)

# Connect the Order with the Transaction
order_transactions = order._transactions
order_transactions.append(Transaction)
