import pygame
import constants as c
import random
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPAY_WIDTH)
        self.vel_x = 0
        self.vel_y = random.randrange(4, 25)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
