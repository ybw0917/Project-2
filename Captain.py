# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for Captain.

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y, symbol="V"):
        Creature.__init__(self, symbol, x, y)
# class Captain(Creature):
#     def __int__(self, x, y, symbol="C"):
#         Creature.__init__(self, symbol, x, y)
        self.__V = []

# Get and set steps
    def getV(self):
        return self.__V

    def setV(self, new_list):
        self.__V = new_list

    def addVeggie(self, veggie):
        self.__V.append(veggie)

    def loseVeggie(self):
        self.__V.pop(-1)
