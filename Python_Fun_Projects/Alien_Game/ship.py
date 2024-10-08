import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        
        if self.moving_right:
            self.x += self.setting.ship_speed
        if self.moving_left:
            self.moving_left -= self.setting.ship_speed
        self.x = self.x
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
