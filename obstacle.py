import pygame
from pygame.sprite import Sprite
from random import randint

class Obstacle(Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            self.fly_1 = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
            self.fly_2 = pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
            self.frames = [self.fly_1, self.fly_2]
            self.y_pos = 180
        else:
            self.snail_1 = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
            self.snail_2 = pygame.image.load('graphics\snail\snail2.png').convert_alpha()
            self.frames = [self.snail_1, self.snail_2]    
            self.y_pos = 300    
            
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (randint(900, 1100), self.y_pos)



    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index//1)]
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


    def update(self):
        self.animation_state()
        self.rect.x -= 5
        self.destroy()