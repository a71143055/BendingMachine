from Beverage import Beverage as BB

class BendingMachine:
    def __init__(self):
        self.__money = 0
        self.__menu = {
            1: BB("콜라", 1000, 10),
            2: BB("사이다", 1000, 10)
        }

    def InputMoney(self, money: int):
        self.__money = money

    def choiceMenu(self):
        try:
            selectedMenu = int(input("메뉴를 선택하세요(0은 종료): "))
            if selectedMenu not in self.__menu and selectedMenu != 0:
                print("유효하지 않은 메뉴입니다.")
                return False, None
            if selectedMenu == 0:
                print("종료합니다.")
                return 0, 0
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

