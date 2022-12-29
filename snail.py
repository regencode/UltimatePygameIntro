import pygame
from random import randint

class Snail:
    def __init__(self):

        self.frame_1 = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
        self.frame_2 = pygame.image.load('graphics\snail\snail2.png').convert_alpha()
        self.animation = [self.frame_1, self.frame_2]
        self.animationIndex = 0
        self.snail_animation_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.snail_animation_timer, 300)

        self.surface = self.animation[self.animationIndex]
        self.rect = self.surface.get_rect()
        self.rect.midbottom = (randint(900, 1100), 300)

    def updateSurface(self):
        if self.animationIndex == 0: self.animationIndex = 1
        else: self.animationIndex = 0
        self.surface = self.animation[self.animationIndex]



