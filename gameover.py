import pygame

class GameOver:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.currentScore = game.score_text.display_score()

        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)

        self.title = self.font.render("Pixel Runner", False, (111, 196, 169)).convert_alpha()
        self.title_rect = self.title.get_rect(center = (400, 75))

        self.stand_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
        self.stand_surface= pygame.transform.rotozoom(self.stand_surface, 0, 2)
        self.stand_rect = self.stand_surface.get_rect(center = (400, 200))

        self.instruction = self.font.render("Click space to start...", False, (111, 196, 169)).convert_alpha()
        self.instruction_rect = self.instruction.get_rect(center = (400, 325))

        self.screen.fill((94, 129, 162))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.stand_surface, self.stand_rect)

        if not int(self.currentScore):
            self.instruction = self.font.render("Click space to start...", False, (111, 196, 169)).convert_alpha()
            self.instruction_rect = self.instruction.get_rect(center = (400, 330))
            self.screen.blit(self.instruction, self.instruction_rect)
        else:
            self.lastScore = self.font.render(f"Score: {str(self.currentScore)}", False, (111, 196, 169)).convert_alpha()
            self.lastScore_rect = self.lastScore.get_rect(center = (400, 330))
            self.screen.blit(self.lastScore, self.lastScore_rect)


