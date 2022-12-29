import sys
import pygame

from random import randint, choice

from gameover import GameOver
from player import Player
from player import PlayerSprite
from obstacle import Obstacle

from score import Score
from snail import Snail
from fly import Fly



class RunnerGame:
    def __init__(self):
        #initialize pygame
        pygame.mixer.init()
        pygame.init()


        #Set display size and caption
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Runner')
        self.screen_rect = self.screen.get_rect()


        #Set clock to limit framerate
        self.clock = pygame.time.Clock()
        self.maxFrameRate = 60

        self.bgm = pygame.mixer.Sound('audio\music.wav')
        self.bgm.play(-1)

        #Creating test surface width=100 and height=200
        #self.test_surface = pygame.Surface((100, 200))

        #However, we can also import an image:
        self.sky = pygame.image.load('graphics/Sky.png').convert_alpha()
        self.ground = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.topleft = (0, 300)
        #Change test_surface color (plain color surface)
        #self.test_surface.fill('Red')


        self.player = Player()
        self.score_text = Score(self)
        self.snail = Snail()
        self.fly = Fly()

        self.playerGroup = pygame.sprite.GroupSingle()
        self.playerGroup.add(PlayerSprite())

        self.obstacle = pygame.sprite.Group()
  

        
        self.obstacle_rect_list = []
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)



        self.gravity = 0 #by default
        self.start_time = 0
        self.game_active = False
        self.run_game()


    def run_game(self):
        while True:
            #Check for keystrokes
            self.checkEvents()

            if self.game_active:
                
                #self.obstacle_rect_list = self.obstacleMovement(self.obstacle_rect_list)

                self.drawSurfaces()
                self.game_active = self.checkCollisions()
                self.score_text.display_score()

                
            else:
                self.end_screen = GameOver(self)
                self.obstacle_rect_list.clear()
                self.player.rect.midbottom = (200, 300)
                self.gravity = 0

                
            #Update the screen 60 times per second
            pygame.display.update()
            self.clock.tick(self.maxFrameRate)


    def drawSurfaces(self):
        self.screen.blit(self.sky, (0, 0))
        #This places the top-left corner of the sky surface to the top left of the screen where x=0 and y=0
        self.screen.blit(self.ground, self.ground_rect)


        #blit text
        pygame.draw.rect(self.screen, "#c0e8ec", self.score_text.font_rect)
        pygame.draw.rect(self.screen, "#c0e8ec", self.score_text.font_rect, 20)
        self.screen.blit(self.score_text.font_surface, self.score_text.font_rect)


        #By assigning a variable to the xpos of the blit, and changing the variable, the screen will keep updating the new snail position, which makes it seem the snail moves to the left.

 

        self.playerGroup.draw(self.screen)
        self.playerGroup.update()

        self.obstacle.draw(self.screen)
        self.obstacle.update()
 
    def checkEvents(self):
        for event in pygame.event.get():
            #if x button is clicked, break the run_game loop and exit the application
            if event.type == pygame.QUIT:
                sys.exit()

            if self.game_active:         
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player.rect.collidepoint(pygame.mouse.get_pos()):
                        self.playerJump()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = True
                    self.start_time = pygame.time.get_ticks()
             
            if self.game_active:
                if event.type == self.obstacle_timer:
                    self.obstacle.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

                if event.type == self.snail.snail_animation_timer:
                    self.snail.updateSurface()
                
                if event.type == self.fly.fly_animation_timer:
                    self.fly.updateSurface()
                
 
    def checkCollisions(self):
        collision_stats = pygame.sprite.spritecollide(self.playerGroup.sprite, self.obstacle, False)
        if collision_stats: 
            self.obstacle.empty()
            return False
        else: return True


if __name__ == "__main__":
    rg = RunnerGame()