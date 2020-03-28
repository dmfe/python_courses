from random import seed
from random import randint
from time import time

class Dice:

    min_edge = 1
    max_edge = 6

    def roll(self):
        return randint(Dice.min_edge, Dice.max_edge)

class Player:

    def __init__(self, dice_count):
        self.__dices = [Dice() for i in range(0, dice_count)]
        self.__dices_values = []
        seed(round(time()))

    def throw_dices(self):
        self.__dices_values = [dice.roll() for dice in self.__dices]

    def dices_sum(self):
        return sum(self.__dices_values)

    def throw_info(self):
        return (f"Dices values: {self.__dices_values}",
                f"Summary value: {self.dices_sum()}")
