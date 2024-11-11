from beverage import Beverage as BB
class BendingMachine:
    def __init__(self, money):
        self.__money = money
        self.__menu = {
            BB("콜라", 1000, 10),
            BB("사이다", 1000, 10)
        }

    def printMenu(self):
        for key, value in self.Menu.items():

            str = "{0}번 : {1} \t {2}원 {3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount() > 0 else "품절"
            )
            print(str+"\n")