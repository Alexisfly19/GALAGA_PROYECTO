import pygame
import constants as c

class Score(pygame.sprite.Sprite):
    def __init__(self, initial_score=0):
        super(Score, self).__init__()
        self.value = initial_score
        self.font_size = 20
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)

        self.x_pad = 24
        self.y_pad = 50

        self.image = self.font.render(f'Score: {self.value}', False, self.color) 
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPAY_WIDTH - self.rect.width - self.x_pad  
        self.rect.y = c.DISPAY_HEIGHT - self.rect.height - self.y_pad  

    def update(self):
        self.image = self.font.render(f'Score: {self.value}', False, self.color) 
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPAY_WIDTH - self.rect.width - self.x_pad 
        self.rect.y = c.DISPAY_HEIGHT - self.rect.height - self.y_pad

    def update_score(self, points):
        self.value += points
        self.update()
