from Beverage import Beverage as BB
class BendingMachine:
    def __init__(self):
        self.__money = 0
        self.__menu = {
            BB("콜라", 1000, 10),
            BB("사이다", 1000, 10)
        }

    def InputMoney(self, money:int):
        self.__money = money
        print(self.__money + "원")

    def choiceMenu(self):
        selectedMenu = input("메뉴를 선택하세요 : ")

        result = selectedMenu in self.__menu.keys()

        return result, selectedMenu

    def printMenu(self):
        for key, value in self.Menu.items():

            str = "{0}번 : {1} \t {2}원 {3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount() > 0 else "품절"
            )
            print(str+"\n")