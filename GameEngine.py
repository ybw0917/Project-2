from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
import pickle
import os
import random


class GameEngine:
    def __init__(self):
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCOREFILE = "highscore.data"
        self.__score = 0
        self.__cpt = None
        self.__snake = None
        self.__field = []
        self.__rabbit_list = []
        self.__veggie_list = []

    def initVeggies(self):
        filename = input("Please enter the name of the vegetable point file: ")
        while not os.path.exists(filename):
            filename = input(f"{filename} does not exist! Please enter the name of the vegetable point file: ")
        with open(filename) as point_file:
            for line in point_file:
                if "Size" in line:          # Read the first line
                    temp = line.split(",")
                    for i in range(int(temp[1])):
                        col = []
                        for j in range(int(temp[2])):
                            col.append(None)
                        self.__field.append(col)
                else:
                    temp = line.split(",")
                    veggie = Veggie(temp[0], temp[1], int(temp[2]))
                    self.__veggie_list.append(veggie)
        for i in range(self.__NUMBEROFVEGGIES):
            y = random.randrange(0, len(self.__field))
            x = random.randrange(0, len(self.__field[1]))
            while self.__field[y][x] is not None:       # make sure the chosen location is not occupied.
                y = random.randrange(0, len(self.__field))
                x = random.randrange(0, len(self.__field[1]))
            type1 = random.randrange(len(self.__veggie_list))
            self.__field[y][x] = self.__veggie_list[type1].getSymbol()

    def initCaptain(self):
        y = random.randrange(0, len(self.__field))
        x = random.randrange(0, len(self.__field[1]))
        while self.__field[y][x] is not None:  # make sure the chosen location is not occupied.
            y = random.randrange(0, len(self.__field))
            x = random.randrange(0, len(self.__field[1]))
        self.__cpt = Captain(x, y)
        self.__field[y][x] = "V"
      

    def initRabbit(self):
        for i in range(self.__NUMBEROFRABBITS):
            y = random.randrange(0, len(self.__field))
            x = random.randrange(0, len(self.__field[1]))
            while self.__field[y][x] is not None:       # make sure the chosen location is not occupied.
                y = random.randrange(0, len(self.__field))
                x = random.randrange(0, len(self.__field[1]))
            rabbit = Rabbit(x, y)
            self.__rabbit_list.append(rabbit)
            self.__field[y][x] = "R"

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbit()

    def remainingVeggies(self):
        count = 0
        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                if self.__field[i][j] is not None and self.__field[i][j] != "V" and self.__field[i][j] != "R":
                    if self.__field[i][j] != "S":
                        count += 1
        return count

    def intro(self):
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before the rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!")
        print()
        print("The vegetables are:")
        for obj in self.__veggie_list:
            print(obj)
        print()
        print("Captain Veggie is V, Rabbits are R's, Snake is S.")
        print()
        print("Good luck!")

    def printField(self):
        border = ""
        for i in range(len(self.__field[1])+2):
            border += "# "
        print(border)
        for i in range(len(self.__field)):
            print("#", end=" ")
            for j in range(len(self.__field[i])):
                if self.__field[i][j] == "V":
                    print(f"\033[34m{self.__field[i][j]}\033[0m", end=" ")
                elif self.__field[i][j] == "R":
                    print(f"\033[31m{self.__field[i][j]}\033[0m", end=" ")
                elif self.__field[i][j] == "S":
                    print(f"\033[33m{self.__field[i][j]}\033[0m", end=" ")
                elif self.__field[i][j] is None:
                    print(" ", end=" ")
                else:
                    print(f"\033[32m{self.__field[i][j]}\033[0m", end=" ")
            print("#")
        print(border)
