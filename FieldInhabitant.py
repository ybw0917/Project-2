class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def __int__(self, symbol):
        self._symbol = symbol

    def getSymbol(self):
        return self._symbol

    def setSymbol(self, newSymbol):
        self._symbol = newSymbol
