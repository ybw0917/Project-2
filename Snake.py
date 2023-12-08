# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for Snake.

from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y, symbol="S"):
        Creature.__init__(self, x, y, symbol)
