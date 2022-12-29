import pygame

class Score:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.current_time = 0

        #create a font for our text -> create text -> blit on screen
        #Font(font_type, font_size)
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)

        #This creates a surface containing our font
        self.font_surface = self.font.render("Score: 00", False, (64,64,64)).convert_alpha()
        self.font_rect = self.font_surface.get_rect()

        self.font_rect.midtop = self.screen_rect.midtop
        self.font_rect.y += 20
    
    def display_score(self):
        if self.game.game_active:
            self.current_time = (pygame.time.get_ticks() - self.game.start_time)//1000
            self.current_time = str(self.current_time)
            self.font_surface = self.font.render(f"Score: {self.current_time}", False, (64,64,64)).convert_alpha()
        return self.current_time


