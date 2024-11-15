from Beverage import Beverage as BB

class BendingMachine:
    def __init__(self):
        self.__money = 0
        self.__name = ""
        self.__menu = {
            1: BB("콜라", 1000, 10),
            2: BB("사이다", 1000, 10),
            3: BB("밀키스", 1000, 10),
            4: BB("밀크티", 1000, 10)
        }

    def InputMoney(self, name: str, money: int):
        self.__name = name
        self.__money = money
        print("이름 :" + self.__name)
        print("잔돈 :" + str(self.__money))

    def choiceMenu(self, selectedMenu):
        try:
            if selectedMenu not in self.__menu:
                print("유효하지 않은 메뉴입니다.")
                return False, None
            if self.__money < self.__menu[selectedMenu].getPrice():
                print("금액이 부족합니다.")
                return False, selectedMenu
            return True, selectedMenu
        except ValueError:
            print("유효한 숫자를 입력해주세요.")
            return False, None

    def OutProduct(self, menu):
        self.__menu[menu].sale()
        print(self.__menu[menu].getName(), "가 나왔습니다.")
        self.__money -= self.__menu[menu].getPrice()

    def printMenu(self):
        for key, value in self.__menu.items():
            str = "{0}번: {1} \t {2}원 {3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount() > 0 else "품절"
            )
            print(str)

    def ReturnMoney(self):
        print("잔돈: " + str(self.__money) + "원")
        return self.__money

