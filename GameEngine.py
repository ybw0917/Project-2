# Author: Bowang Yan, Yu Zhuang, Shengwei Duan
# Date: 12/07/2023
# Description:  Class File for GameEngine.

from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
import pickle
import os
import random


class GameEngine:
    def __init__(self):
        self.__NUMBEROFVEGGIES = 30    # Number of veggies.
        self.__NUMBEROFRABBITS = 5    # Number of rabbits.
        self.__HIGHSCOREFILE = "highscore.data"
        self.__score = 0    # Points the player has got.
        self.__cpt = None
        self.__snake = None
        self.__field = []
        self.__rabbit_list = [] # List stores all the rabbit objects.
        self.__veggie_list = [] # List stores all the veggie objects. 

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
            self.__field[y][x] = self.__veggie_list[type1].getSymbol()  # Fill the fields with Symbols

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
            
    def initSnake(self):
        pass

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbit()
        self.initSnake()

    def remainingVeggies(self):
        count = 0
        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                if self.__field[i][j] is not None and self.__field[i][j] != "V" and self.__field[i][j] != "R":
                    if self.__field[i][j] != "S":
                        # Make sure the counter only counts vegetables remain.
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
                    print(f"\033[34m{self.__field[i][j]}\033[0m", end=" ")  # Print Captain in blue color.
                elif self.__field[i][j] == "R":
                    print(f"\033[31m{self.__field[i][j]}\033[0m", end=" ")  # Print Rabbits in red color.
                elif self.__field[i][j] == "S":
                    print(f"\033[33m{self.__field[i][j]}\033[0m", end=" ")  # Print Snake in yellow color.
                elif self.__field[i][j] is None:
                    print(" ", end=" ")
                else:
                    print(f"\033[32m{self.__field[i][j]}\033[0m", end=" ")  # Print Veggies in green color.
            print("#")
        print(border)

    def getScore(self):
        return self.__score

    def moveRabbits(self):
        for rabbit in self.__rabbit_list:
            flag = 0    # Show if the object can move normally.
            direction = random.randint(0, 1)        # 0: horizontal, 1:vertical
            distance = random.randint(-1, 1)        # -1: left or up, 0:no movement, 1: right or down
            if direction == 0:          # move horizontally
                if distance == 0:
                    continue
                else:
                    newX = rabbit.getX() + distance
                    if newX < 0 or newX >= len(self.__field[0]):    # rabbit tries to cross left or right border
                        flag = 1
                    for i in self.__rabbit_list:
                        if i.getX() == newX and i.getY() == rabbit.getY():    # rabbit tries to step on other rabbits
                            flag = 1
                            break
                        elif newX == self.__cpt.getX() and rabbit.getY() == self.__cpt.getY():
                            # rabbit tries to step on Captain
                            flag = 1
                            break
                        elif newX == self.__snake.getX() and rabbit.getY() == self.__snake.getY():
                            # rabbit tries to step on Snake
                            flag = 1
                            break
                    if flag == 0:
                        self.__field[rabbit.getY()][rabbit.getX()] = None
                        rabbit.setX(newX)
            if direction == 1:          # move vertically
                if distance == 0:
                    continue
                else:
                    newY = rabbit.getY()+distance
                    if newY < 0 or newY >= len(self.__field):   # rabbit tries to cross up or down border
                        flag = 1
                    for i in self.__rabbit_list:
                        if i.getY() == newY and i.getX() == rabbit.getX():    # rabbit tries to step on other rabbits
                            flag = 1
                            break
                        elif newY == self.__cpt.getY() and rabbit.getX() == self.__cpt.getX():
                            # rabbit tries to step on Captain
                            flag = 1
                            break
                        elif newY == self.__snake.getY() and rabbit.getX() == self.__snake.getX():
                            # rabbit tries to step on Snake
                            flag = 1
                            break
                    if flag == 0:
                        self.__field[rabbit.getY()][rabbit.getX()] = None
                        rabbit.setY(newY)
        for rabbit in self.__rabbit_list:
            self.__field[rabbit.getY()][rabbit.getX()] = "R"    # Fill the fields with rabbits.

    def moveCptVertical(self, ver_val):
        flag = 0    # Show if the object can move normally.
        newY = self.__cpt.getY() + ver_val
        if newY < 0 or newY >= len(self.__field):   # Tries to go out of the boundaries.
            print("You can't go that way!")
            flag = 1
        elif self.__field[newY][self.__cpt.getX()] == "R":          # Avoid stepping on rabbits
            flag = 1
            print("Don't step on the bunnies!")
        elif self.__field[newY][self.__cpt.getX()] == "S":          # Stepping on Snake will lose points
            if len(self.__cpt.getV()) >= 5:
                for i in range(-5, 0):
                    self.__score -= self.__cpt.getV()[i].getValue()
                for i in range(5):
                    self.__cpt.getV().pop(-1)
            else:
                for i in range(-len(self.__cpt.getV()), 0):
                    self.__score -= self.__cpt.getV()[i].getValue()
                for i in range(len(self.__cpt.getV())):
                    self.__cpt.getV().pop(-1)
            print("Ops, Captain was caught by the Snake!")
            self.initSnake()
            self.__field[newY][self.__cpt.getX()] = "V"
            self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        elif self.__field[newY][self.__cpt.getX()] is None:
            self.__field[newY][self.__cpt.getX()] = "V"
            self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        else:
            for veggie in self.__veggie_list:
                if self.__field[newY][self.__cpt.getX()] == veggie.getSymbol():
                    print(f"Yummy! A delicious {veggie.getName()}")
                    self.__cpt.addVeggie(veggie)
                    self.__score += veggie.getValue()
                    self.__field[newY][self.__cpt.getX()] = "V"
                    self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        if flag == 0:
            self.__cpt.setY(newY)

    def moveCptHorizontal(self, hor_val):
        flag = 0
        newX = self.__cpt.getX() + hor_val
        if newX < 0 or newX >= len(self.__field[0]):    # Tries to go out of the boundaries.
            print("You can't go that way!")
            flag = 1
        elif self.__field[self.__cpt.getY()][newX] == "R":
            print("Don't step on the bunnies!")
            flag = 1
        elif self.__field[self.__cpt.getY()][newX] == "S":  # Stepping on Snake will lose points
            if len(self.__cpt.getV()) >= 5:
                for i in range(-5, 0):
                    self.__score -= self.__cpt.getV()[i].getValue()
                for i in range(5):
                    self.__cpt.getV().pop(-1)
            else:
                for i in range(-len(self.__cpt.getV()), 0):
                    self.__score -= self.__cpt.getV()[i].getValue()
                for i in range(len(self.__cpt.getV())):
                    self.__cpt.getV().pop(-1)
            print("Ops, Captain was caught by the Snake!")
            self.initSnake()
            self.__field[self.__cpt.getX()][newX] = "V"
            self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        elif self.__field[self.__cpt.getY()][newX] is None:
            self.__field[self.__cpt.getY()][newX] = "V"
            self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        else:
            for veggie in self.__veggie_list:
                if self.__field[self.__cpt.getY()][newX] == veggie.getSymbol():
                    print(f"Yummy! A delicious {veggie.getName()}")
                    self.__cpt.addVeggie(veggie)
                    self.__score += veggie.getValue()
                    self.__field[self.__cpt.getY()][newX] = "V"
                    self.__field[self.__cpt.getY()][self.__cpt.getX()] = None
        if flag == 0:
            self.__cpt.setX(newX)
    
    def moveCaptain(self):
        movement = input("Would you like to move up(W), down(S), left(A), or right(D):")
        if movement == "W" or movement == "w":
            self.moveCptVertical(-1)
        elif movement == "S" or movement == "s":
            self.moveCptVertical(1)
        elif movement == "A" or movement == "a":
            self.moveCptHorizontal(-1)
        elif movement == "D" or movement == "d":
            self.moveCptHorizontal(1)
        else:
            print(f"{movement} is not a valid option")
        self.moveRabbits()
        self.moveSnake()

    def moveSnake(self):
        flag = 0
        if self.__snake.getX() > self.__cpt.getX():
            newX = self.__snake.getX()-1
            if self.__field[self.__snake.getY()][newX] != "V":
                if self.__field[self.__snake.getY()][newX] is not None:
                    flag = 1
            else:
                if len(self.__cpt.getV()) >= 5:
                    for i in range(-5, 0):
                        self.__score -= self.__cpt.getV()[i].getValue()
                    for i in range(5):
                        self.__cpt.getV().pop(-1)
                else:
                    for i in range(-len(self.__cpt.getV()), 0):
                        self.__score -= self.__cpt.getV()[i].getValue()
                    for i in range(len(self.__cpt.getV())):
                        self.__cpt.getV().pop(-1)
                self.__field[self.__snake.getY()][self.__snake.getX()] = None
                print("Ops, Captain was caught by the Snake!")
                self.initSnake()
            if flag == 0:
                self.__field[self.__snake.getY()][self.__snake.getX()] = None
                self.__snake.setX(newX)
                self.__field[self.__snake.getY()][self.__snake.getX()] = "S"
        elif self.__snake.getX() < self.__cpt.getX():
            newX = self.__snake.getX()+1
            if self.__field[self.__snake.getY()][newX] != "V":
                if self.__field[self.__snake.getY()][newX] is not None:
                    flag = 1
            else:
                if len(self.__cpt.getV()) >= 5:
                    for i in range(-5, 0):
                        self.__score -= self.__cpt.getV()[i].getValue()
                    for i in range(5):
                        self.__cpt.getV().pop(-1)
                else:
                    for i in range(-len(self.__cpt.getV()), 0):
                        self.__score -= self.__cpt.getV()[i].getValue()
                    for i in range(len(self.__cpt.getV())):
                        self.__cpt.getV().pop(-1)
                self.__field[self.__snake.getY()][self.__snake.getX()] = None
                print("Ops, Captain was caught by the Snake!")
                self.initSnake()
            if flag == 0:
                self.__field[self.__snake.getY()][self.__snake.getX()] = None
                self.__snake.setX(newX)
                self.__field[self.__snake.getY()][self.__snake.getX()] = "S"
        else:
            if self.__snake.getY() > self.__cpt.getY():
                newY = self.__snake.getY()-1
                if self.__field[newY][self.__snake.getX()] != "V":
                    if self.__field[newY][self.__snake.getX()] is not None:
                        flag = 1
                else:
                    flag = 1
                    if len(self.__cpt.getV()) >= 5:
                        for i in range(-5, 0):
                            self.__score -= self.__cpt.getV()[i].getValue()
                        for i in range(5):
                            self.__cpt.getV().pop(-1)
                    else:
                        for i in range(-len(self.__cpt.getV()), 0):
                            self.__score -= self.__cpt.getV()[i].getValue()
                        for i in range(len(self.__cpt.getV())):
                            self.__cpt.getV().pop(-1)
                    self.__field[self.__snake.getY()][self.__snake.getX()] = None
                    print("Ops, Captain was caught by the Snake!")
                    self.initSnake()
                if flag == 0:
                    self.__field[self.__snake.getY()][self.__snake.getX()] = None
                    self.__snake.setY(newY)
                    self.__field[self.__snake.getY()][self.__snake.getX()] = "S"
            elif self.__snake.getY() < self.__cpt.getY():
                newY = self.__snake.getY()+1
                if self.__field[newY][self.__snake.getX()] != "V":
                    if self.__field[newY][self.__snake.getX()] is not None:
                        flag = 1
                else:
                    flag = 1
                    if len(self.__cpt.getV()) >= 5:
                        for i in range(-5, 0):
                            self.__score -= self.__cpt.getV()[i].getValue()
                        for i in range(5):
                            self.__cpt.getV().pop(-1)
                    else:
                        for i in range(-len(self.__cpt.getV()), 0):
                            self.__score -= self.__cpt.getV()[i].getValue()
                        for i in range(len(self.__cpt.getV())):
                            self.__cpt.getV().pop(-1)
                    self.__field[self.__snake.getY()][self.__snake.getX()] = None
                    print("Ops, Captain was caught by the Snake!")
                    self.initSnake()
                if flag == 0:
                    self.__field[self.__snake.getY()][self.__snake.getX()] = None
                    self.__snake.setY(newY)
                    self.__field[self.__snake.getY()][self.__snake.getX()] = "S"


    def gameOver(self):
        if self.remainingVeggies() == 0:
            print("Game over!")
            print("You managed to harvest the following vegetables:")
            for i in self.__cpt.getV():
                print(i.getName())
            print(f"Your score was: {self.getScore()}")

    def highScore(self):
        if not os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "wb") as file:
                initial = input("Please enter your three initials to go on the scoreboard: ")
                high_score = (initial, self.__score)
                high_score_list = [high_score]
                pickle.dump(high_score_list, file)
        else:
            with open(self.__HIGHSCOREFILE, "rb") as file:
                high_score_list = pickle.load(file)
            initial = input("Please enter your three initials to go on the scoreboard: ")
            high_score = (initial, self.__score)
            for i in range(len(high_score_list)):
                if high_score[1] > high_score_list[i][1]:
                    high_score_list.insert(i, high_score)
            with open(self.__HIGHSCOREFILE, "wb") as file:
                pickle.dump(high_score_list, file)
        print("HIGH SCORES")
        print("Name\tScore")
        for i in range(len(high_score_list)):
            print(f"{high_score_list[i][0]}\t\t{high_score_list[i][1]}")




