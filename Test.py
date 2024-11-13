from BendingMachine import BendingMachine

if __name__ == "__main__":
    BM = BendingMachine()
    BM.InputMoney(10000)

    while(True):
        BM.printMenu()
        isOk = False
        while not isOk:
            selectedMenu = int(input("메뉴를 선택하세요(0은 종료): "))
            if selectedMenu == 0:
                print("종료합니다.")
                quit()
            isOk, menu = BM.choiceMenu(selectedMenu)
        print("{0}번 : {1}".format(menu, BM._BendingMachine__menu[menu].getName()))
        BM.OutProduct(menu)
        if BM.ReturnMoney() < 0:
            quit()