from BendingMachine import BendingMachine

if __name__ == "__main__":
    BM = BendingMachine()
    BM.printMenu()
    BM.InputMoney()

    isOk, menu = BM.choiceMenu()