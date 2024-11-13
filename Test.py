from BendingMachine import BendingMachine

if __name__ == "__main__":
    BM = BendingMachine()
    BM.printMenu()
    BM.InputMoney(1000)
    isOk = False
    while not isOk:
        isOk, menu = BM.choiceMenu()
    print("{0}번 : {1}".format(menu, BM._BendingMachine__menu[menu].getName()))
    BM.OutProduct(menu)
    BM.ReturnMoney()
