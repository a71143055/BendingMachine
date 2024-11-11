from beverage import Beverage as BB
class BendingMachine:
    def __init__(self, money):
        self.__money = money
        self.__menu = []

    def setMenu(self, name, price, count):
        BB.__name = name
        BB.__price = price
        BB.__count = count
        BB.__salesCount = 0