from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y, symbol="R"):
        Creature.__init__(self, symbol, x, y)
