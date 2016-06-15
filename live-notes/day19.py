class BankAccount:
    def __init__(self):
        pass

    def withdraw(self):
        pass


class SubBankAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__()
        self.stuff
