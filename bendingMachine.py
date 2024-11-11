from beverage import Beverage as BB
class BendingMachine:
    def __init__(self, money):
        self.__money = money
        self.__menu = []

    def setMenu(self, name, price, count):
        self.__menu += BB(name, price,count)

    def getMenu(self):
        return self.__menu