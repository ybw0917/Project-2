# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for Rabbit.

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y, symbol="R"):
        Creature.__init__(self, x, y,symbol)
