import pygame
import time

from pygame.locals import *
from FirstGame.player import Player
from FirstGame.platform import Platform
from FirstGame.line_part import Linepart
from FirstGame.part import Part
from datetime import datetime


class Window(object):



    def __init__(self, x=1280, y=960):

        self.running = True
        self.end = False

        # Initialization of pygame
        pygame.init()

        # Initialization of text parameters
        self.myfont = pygame.font.SysFont('Arial', 30)

        # Initialization of time parameters
        self.now = datetime.now()

        # Initialize platforms
        self.plat_img = []
        list_line_part = [Linepart('mainline', [Part(200, 700, 1),
                          Part(232, 700, 2),
                          Part(264, 700, 2),
                          Part(296, 700, 2),
                          Part(328, 700, 2),
                          Part(360, 700, 2),
                          Part(392, 700, 2),
                          Part(424, 700, 2),
                          Part(456, 700, 2),
                          Part(488, 700, 2),
                          Part(520, 700, 2),
                          Part(552, 700, 2),
                          Part(584, 700, 2),
                          Part(616, 700, 2),
                          Part(648, 700, 2),
                          Part(680, 700, 2),
                          Part(712, 700, 2),
                          Part(744, 700, 2),
                          Part(776, 700, 2),
                          Part(808, 700, 2),
                          Part(840, 700, 2),
                          Part(872, 700, 2),
                          Part(904, 700, 2),
                          Part(936, 700, 2),
                          Part(968, 700, 3)], 700)]
        self.platforms = Platform(list_line_part)

        # Initialize window
        self._x = x
        self._y = y

        self.fenetre = pygame.display.set_mode((self._x, self._y))

        self.fond = pygame.image.load("FirstGame/venv/resources/BG.png").convert()

        # Initialize image
        self.plat_img.append(pygame.transform.scale(
            pygame.image.load(Part.get_img_path('pp1')).convert_alpha(), (32, 32)))
        self.plat_img.append(
            pygame.transform.scale(pygame.image.load(Part.get_img_path('pp2')).convert_alpha(), (32, 32)))
        self.plat_img.append(
            pygame.transform.scale(pygame.image.load(Part.get_img_path('pp3')).convert_alpha(), (32, 32)))
        self.caisse = pygame.image.load("FirstGame/venv/resources/Objects/Crate.png").convert_alpha()
        self.cactus = pygame.transform.scale(pygame.image.load("FirstGame/venv/resources/Objects/Cactus (2).png")
                                             .convert_alpha(), (35, 23))

        # Initialize player
        self.player = Player(264, 668)

    def run(self):

        duree = 0

        while self.running:

            if not self.end:

                duree = datetime.now() - self.now

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.close_window()
                    if event.type == KEYDOWN and event.key == K_z:
                        if not self.player.get_y() < 668:
                            self.player.jump()
                    elif event.type == KEYDOWN and event.key == K_d:
                        self.player.change_appearence('right')
                    elif event.type == KEYDOWN and event.key == K_q:
                        self.player.change_appearence('left')

                key = pygame.key.get_pressed()
                if key[pygame.K_d] and not self.limits('x'):
                    self.player.move_x(1)
                elif key[pygame.K_q] and not self.limits('-x'):
                    self.player.move_x(-1)

                if self.player.bool_jump() and not self.limits('-y'):
                    self.player.move_y(-1)
                elif self.platforms.get_list_line_part()[0].get_list_part()[0].get_x() < self.player.get_x() < \
                     self.platforms.get_list_line_part()[0].get_list_part()[
                         len(self.platforms.get_list_line_part()[0].get_list_part()) - 1].get_x() + 32:
                    if self.player.get_y()+32 < self.platforms.get_list_line_part()[0].get_list_part()[0].get_y():
                        self.player.gravity()
                else:
                    if self.player.get_y() < self.platforms.get_list_line_part()[0].get_list_part()[0].get_y() + 32:
                        self.player.gravity()
            else:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.close_window()

            self.initialize_ground()

            pos = (self.player.get_x(), self.player.get_y())

            af_player = pygame.image.load(self.player.image).convert_alpha()

            text = self.myfont.render(str(duree), False, (0, 0, 0))

            self.fenetre.blit(text, (1000, 10))

            self.fenetre.blit(af_player, pos)

            self.verify_loose()

            pygame.display.flip()

    def initialize_ground(self):

        self.fenetre.blit(self.fond, (0, 0))

        for linepart in self.platforms.get_list_line_part():
            for part in linepart.get_list_part():
                self.fenetre.blit(self.plat_img[part.get_img() - 1], (part.get_x(), part.get_y()))

        self.fenetre.blit(self.cactus, (936, 677))

        # for part in self.platforms.get_list_line_part().get_list_part():
            # self.fenetre.blit(self.plat_img[part.get_img()-1], (part.get_x(), part.get_y()))

    def game_over(self):

        self.player.change_appearence('stay')
        text = self.myfont.render('GAME OVER', False, (0, 0, 0))

        self.fenetre.blit(text, (534, 440))

    def bool_fall(self):

        posxrplayer = self.player.get_x()+32
        posxlplayer = self.player.get_x()
        posyplayer = self.player.get_y()+32

        limitxl = self.platforms.get_list_line_part()[0].get_list_part()[0].get_x()
        limitxr = self.platforms.get_list_line_part()[0].get_list_part()[len(self.platforms.get_list_line_part()[0].get_list_part())-1].get_x()+32
        limity = self.platforms.get_list_line_part()[0].get_list_part()[0].get_y()+32

        if (posxlplayer < limitxl and posyplayer > limity) or (posxrplayer > limitxr and posyplayer > limity):
            return True
        else:
            return False

    def touch_enemy(self):

        p1 = (self.player.get_x(), self.player.get_y())
        p2 = (self.player.get_x() + 32, self.player.get_y())
        p3 = (self.player.get_x(), self.player.get_y() + 32)
        p4 = (self.player.get_x() + 32, self.player.get_y() + 32)

        player_limits = [p1, p2, p3, p4]

        for pos in player_limits:
            if (936, 677) <= pos <= (971, 700):
                return True
            else:
                return False

        # if posxlplayer < 936 + 28 and posxrplayer > 942 and posyplayer < 676 and posyplayer > 700:
        #    return True
        # else:
        #     return False

        # posxrplayer = self.player.get_x() + 32
        # posxlplayer = self.player.get_x()
        # posyplayer = self.player.get_y() + 32

        # if posxlplayer < 936+28 and posxrplayer > 942 and posyplayer < 676 and posyplayer > 700:
        #    return True
        # else:
        #    return False

    def verify_loose(self):

        if self.bool_fall():
            while self.player.get_y() < 732:
                self.player.gravity()
            self.end = True

        if self.touch_enemy():
            self.end = True

        if self.end:
            self.game_over()

    def solid_platform(self):

        if self.player.get_x()+32 < self.platforms.get_list_line_part()[0].get_list_part()[0].get_x() \
                or self.player.get_x() > self.platforms.get_list_line_part()[0].get_list_part()[len(self.platforms.get_list_line_part()[0].get_list_part())-1].get_x()+32:
            return True
        else:
            return False

    def limits(self, type):

        overlimit = False
        limitsx = [self._x]
        limitsy = [self._y]
        limits_x = [0]
        limits_y = [0]
        # mx = 1280

        if type == 'x':
            for limitx in limitsx:
                if self.player.get_x() + 16 > limitx:
                    overlimit = True
            if self.bool_fall():
                overlimit = True
        elif type == '-x':
            for limit_x in limits_x:
                if self.player.get_x() + 16 < limit_x:
                    overlimit = True
            if self.bool_fall():
                overlimit = True
        elif type == 'y':
            for limity in limitsy:
                if self.player.get_y() + 16 > limity:
                    overlimit = True
            if self.bool_fall():
                overlimit = True
        elif type == '-y':
            for limit_y in limits_y:
                if self.player.get_y() + 16 < limit_y:
                    overlimit = True
            if self.bool_fall():
                overlimit = True

        return overlimit

    def close_window(self):
        self.running = False
