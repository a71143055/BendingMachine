from Beverage import Beverage as BB
class BendingMachine:
    def __init__(self):
        self.__money = 0
        self.__menu = {
            1 : BB("콜라", 1000, 10),
            2 : BB("사이다", 1000, 10)
        }

    def InputMoney(self, money:int):
        self.__money = money
        print(str(self.__money) + "원")

    def choiceMenu(self):
        selectedMenu = int(input("메뉴를 선택하세요 : "))
        result = selectedMenu in self.__menu.keys()
        if result == True:
            if self.__money < self.__menu[selectedMenu].getPrice():
                result = False
                print("금액이 부족합니다.")

        return result, selectedMenu

    def OutProduct(self, menu):
        self.__menu[menu].sale()
        print(self.__menu[menu].getName(), "가 나왔습니다.")

        self.__money -= self.__menu[menu].getPrice()
        isContinue = False

    def printMenu(self):
        for key, value in self.__menu.items():

            str = "{0}번 : {1} \t {2}원 {3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount() > 0 else "품절"
            )
            print(str+"\n")

    def ReturnMoney(self):
        tmp = self.__money
        self.__money = 0