from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y, symbol="S"):
        Creature.__init__(self, x, y, symbol)
