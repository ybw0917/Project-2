# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for Veggie.

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, value):
        FieldInhabitant.__init__(self, symbol)
        self.__name = name
        self.__value = value

    def getValue(self):
        return self.__value

    def getName(self):
        return self.__name

    def setValue(self, newValue):
        self.__value = newValue

    def setName(self, newName):
        self.__name = newName

    def __str__(self):
        return f"{self.getSymbol()}: {self.getName()}   ,{self.getValue()} points"

