import pygame
import constants as c 
from star import Star
from planet import Planet
import random


class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (0, 0, 15)# Color oscuro para el fondo
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.planet_timer = random.randrange(420, 720)  # 7-12 seconds
        self.max_planet = 3
        self.current_num_planets = 0  # typo corregido


    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.DISPAY_HEIGHT:
                self.planets.remove(planet)
                self.current_num_planets -= 1
        if self.planet_timer == 0:
            if self.current_num_planets < self.max_planet:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(420, 720)  # 7-12 seconds
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.DISPAY_HEIGHT:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.planets.draw(self.image)
        self.stars.draw(self.image)
        self.planet_timer -= 1
        self.star_timer -= 1

