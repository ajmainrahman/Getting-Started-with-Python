class Transaction:
    def __init__(self,date, Ordernumber):
        self._date = date
        self._Ordernumber = Ordernumber
    def loadaccounthistory(self):
        print("Accout History loaded")
    def loadopenorder(self):
        print("Open order loaded")
transaction = Transaction("2023-05-28","Order9090")
transaction.loadopenorder()
transaction.loadaccounthistory()