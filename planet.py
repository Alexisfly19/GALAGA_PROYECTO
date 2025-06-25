import pygame
import constants as c
import random

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet_01 = pygame.image.load("planet_01.PNG").convert_alpha()
        self.planet_02 = pygame.image.load("planet_02.PNG").convert_alpha()
        self.planet_03 = pygame.image.load("planet_03.PNG").convert_alpha()
        self.planet_04 = pygame.image.load("planet_04.PNG").convert_alpha()
        self.planet_05 = pygame.image.load("planet_05.PNG").convert_alpha()
        self.planet_06 = pygame.image.load("planet_06.PNG").convert_alpha()
        self.planet_07 = pygame.image.load("planet_07.PNG").convert_alpha()
        self.planet_08 = pygame.image.load("planet_08.PNG").convert_alpha()
        self.planet_09 = pygame.image.load("planet_09.PNG").convert_alpha()


        self.img_planets = [
            self.planet_01,
            self.planet_02,
            self.planet_03,
            self.planet_04,
            self.planet_05,
            self.planet_06,
            self.planet_07,
            self.planet_08,
            self.planet_09]
        
        self.num_planets = len(self.img_planets) # Número de planetas disponibles
        self.img_index = random.randrange(0, self.num_planets - 1) 
        self.image = self.img_planets[self.img_index] # Carga una imagen de planeta aleatoria
        self.scale_value = random.uniform(0.25, 1.0)  # Escala aleatoria entre 0.25 y 1.0 
        self.image = pygame.transform.scale(self.image, (int((self.image.get_width() * self.scale_value)),
                                            int(self.image.get_height() * self.scale_value)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPAY_WIDTH - self.rect.width) 
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, c.DISPAY_WIDTH - self.rect.width)
        self.pos_y = 0 - self.rect.height
        self.vel_x = 0.0
        self.vel_y = random.uniform(1.0, 1.5)  # Velocidad vertical aleatoria


    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)


