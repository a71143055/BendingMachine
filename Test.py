from BendingMachine import BendingMachine

if __name__ == "__main__":
    BM = BendingMachine()
    BM.printMenu()
    BM.InputMoney(1000)
    isOk = False
    while(isOk == False):
        isOk, menu = BM.choiceMenu()
    print("{0}번 : {1}".format(isOk,BM.choiceMenu()))