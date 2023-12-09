# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for FieldInhabitant.

class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def __int__(self, symbol):
        self._symbol = symbol

    # Getter and setter functions
    def getSymbol(self):
        return self._symbol

    def setSymbol(self, newSymbol):
        self._symbol = newSymbol
