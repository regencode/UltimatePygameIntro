import pygame
from random import randint

class Fly:
    def __init__(self):


        self.frame_1 = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
        self.frame_2 = pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
        self.animation = [self.frame_1, self.frame_2]
        self.animationIndex = 0

        self.fly_animation_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.fly_animation_timer, 500)

        self.surface = self.animation[self.animationIndex]
        self.rect = self.surface.get_rect(bottomright = (randint(900, 1100), 150))


    def updateSurface(self):
        if self.animationIndex == 0: self.animationIndex = 1
        else: self.animationIndex = 0
        self.surface = self.animation[self.animationIndex]
