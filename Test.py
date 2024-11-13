from BendingMachine import BendingMachine

if __name__ == "__main__":
    BM = BendingMachine()
    BM.InputMoney(10000)

    while(True):
        BM.printMenu()
        isOk = False
        while not isOk:
            isOk, menu = BM.choiceMenu()
        print("{0}번 : {1}".format(menu, BM._BendingMachine__menu[menu].getName()))
        BM.OutProduct(menu)