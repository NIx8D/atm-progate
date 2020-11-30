from card import AtmCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id;
        self.pin = custPin
        self.balance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance

    def witdrawalBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal

    def setNewPin(self, newPin):
        self.pin = newPin

    