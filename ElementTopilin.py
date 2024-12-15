class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def dump(self):
        print(f"Элемент: {self.__name}, Символ: {self.__symbol}, Номер: {self.__number}")

vanadium = ElementФамилия("Ванадий", "V", 23)

vanadium.dump()
