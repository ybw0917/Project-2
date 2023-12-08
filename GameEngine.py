from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake
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
