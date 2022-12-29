import pygame
from pygame.sprite import Sprite

class Player:
    def __init__(self):
        self.player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        self.player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()

        self.player_walk = [self.player_walk1, self.player_walk2]
        self.player_walk_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png')

        #Create a rectangle that is the same size as the surface
        self.surface = self.player_walk[self.player_walk_index]
        self.rect = self.surface.get_rect()
        self.rect.midbottom = (200, 300)
    
    def player_animation(self):
        # play walking animation if player is on floor
        # display the jump surface when player is not on floor

        if self.rect.bottom < 300: # player not on floor
            self.surface = self.player_jump
        
        else: # player on floor
            # walk animation
            self.player_walk_index += 0.1
            if self.player_walk_index//1 >= len(self.player_walk):
                self.player_walk_index = 0
            self.surface = self.player_walk[int(self.player_walk_index//1)]

class PlayerSprite(Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        self.player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()


        self.player_walk = [self.player_walk1, self.player_walk2]
        self.player_walk_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png')


        self.image = self.player_walk[self.player_walk_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (200, 300)

        self.gravity = 0 #default

        self.jump_sound = pygame.mixer.Sound('audio\jump.wav')
        self.jump_sound.set_volume(0.5)


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()


    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_walk_index += 0.1
            if self.player_walk_index//1 >= len(self.player_walk):
                self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index//1)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()