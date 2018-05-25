import pygame
import time
import random

class Player(object):

    stay = 'FirstGame/venv/resources/blocky/blocky.png'
    left = 'FirstGame/venv/resources/blocky/blocky_left.png'
    right = 'FirstGame/venv/resources/blocky/blocky_right.png'
    jheight = 0

    def __init__(self, x=232, y=700):

        self._x = x
        self._y = y
        self.image = self.stay

    def move_x(self, value):
        self._x += value
        self.increase_jump(-0.25)

    def move_y(self, value):
        self._y += value
        self.increase_jump(-1)

    def gravity(self):
        self.move_y(+1)

    def jump(self):
        if not self.bool_jump():
            self.jheight = 80

    def increase_jump(self, number):
        if self.bool_jump():
            self.jheight += number

    def bool_jump(self):
        if self.jheight > 0:
            return True
        else:
            return False

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def change_appearence(self, mode):
        if mode == 'right':
            self.image = self.right
        elif mode == 'left':
            self.image = self.left
        elif mode == 'stay':
            self.image = self.stay
