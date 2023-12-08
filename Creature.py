# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for FieldInhabitant.

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        FieldInhabitant.__init__(self, symbol)
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, newX):
        self._x = newX

    def setY(self, newY):
        self._y = newY
