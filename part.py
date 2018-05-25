import pygame

class Part(object):

    pp1 = 'FirstGame/venv/resources/Tile/1.png'
    pp2 = 'FirstGame/venv/resources/Tile/2.png'
    pp3 = 'FirstGame/venv/resources/Tile/3.png'
    pp4 = 'FirstGame/venv/resources/Tile/4.png'
    pp5 = 'FirstGame/venv/resources/Tile/5.png'
    pp6 = 'FirstGame/venv/resources/Tile/6.png'
    pp7 = 'FirstGame/venv/resources/Tile/7.png'
    pp8 = 'FirstGame/venv/resources/Tile/8.png'
    pp9 = 'FirstGame/venv/resources/Tile/9.png'
    pp10 = 'FirstGame/venv/resources/Tile/10.png'
    pp11 = 'FirstGame/venv/resources/Tile/11.png'
    pp12 = 'FirstGame/venv/resources/Tile/12.png'
    pp13 = 'FirstGame/venv/resources/Tile/13.png'
    pp14 = 'FirstGame/venv/resources/Tile/14.png'
    pp15 = 'FirstGame/venv/resources/Tile/15.png'
    pp16 = 'FirstGame/venv/resources/Tile/16.png'

    def __init__(self, x, y, img):

        self._x = x
        self._y = y
        self._img = img

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_img(self):
        return self._img

    @staticmethod
    def get_img_path(id):

        if id == 'pp1':
            return 'FirstGame/venv/resources/Tile/1.png'
        elif id == 'pp2':
            return 'FirstGame/venv/resources/Tile/2.png'
        elif id == 'pp3':
            return 'FirstGame/venv/resources/Tile/3.png'
        elif id == 'pp4':
            return 'FirstGame/venv/resources/Tile/4.png'
        elif id == 'pp5':
            return 'FirstGame/venv/resources/Tile/5.png'
        elif id == 'pp6':
            return 'FirstGame/venv/resources/Tile/6.png'
        elif id == 'pp7':
            return 'FirstGame/venv/resources/Tile/7.png'
        elif id == 'pp8':
            return 'FirstGame/venv/resources/Tile/8.png'
        elif id == 'pp9':
            return 'FirstGame/venv/resources/Tile/9.png'
        elif id == 'pp10':
            return 'FirstGame/venv/resources/Tile/10.png'
        elif id == 'pp11':
            return 'FirstGame/venv/resources/Tile/11.png'
        elif id == 'pp12':
            return 'FirstGame/venv/resources/Tile/12.png'
        elif id == 'pp13':
            return 'FirstGame/venv/resources/Tile/13.png'
        elif id == 'pp14':
            return 'FirstGame/venv/resources/Tile/14.png'
        elif id == 'pp15':
            return 'FirstGame/venv/resources/Tile/15.png'
        elif id == 'pp16':
            return 'FirstGame/venv/resources/Tile/16.png'
