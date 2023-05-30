class Order:
    def __init__(self, date, delivery_instruction, order_number):
        self._date = date
        self._delivery_instruction = delivery_instruction
        self._order_number = order_number

    def check_for_outstanding_order(self):
        print("You are great")
order = Order("2023-05-28", "Handle with care","Order1234")

order.check_for_outstanding_order()
