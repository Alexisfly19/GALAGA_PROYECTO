import pygame
import constants as c
from health_bar import HealthBar
from heart_icon import HeartIcon
from score import Score
from lives import Lives  


class HUD:
    def __init__(self, hp, lives):
        bar_x = 80
        bar_y = c.DISPLAY_SIZE[1] - 29  # Ajusta según el alto de la barra

        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = bar_x
        self.health_bar.rect.y = bar_y

        self.health_bar_group = pygame.sprite.Group(self.health_bar)

        heart_icon_size = 48  # Igual que en HeartIcon
        heart_x = bar_x  # MISMA X QUE LA BARRA
        heart_y = bar_y - heart_icon_size - 10  # ARRIBA DE LA BARRA, 10px de separación
        self.heart_icon = HeartIcon(x=heart_x, y=heart_y)

        self.lives = Lives(lives)
        self.lives.rect.x = 230  # Ajusta la posición X según sea necesario
        self.lives.rect.y = c.DISPAY_HEIGHT - 50  # Ajusta la posición Y según sea necesario

        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.lives)
        self.icons_group.add(self.heart_icon) 

        self.score = Score()
        self.score_group = pygame.sprite.Group(self.score)  # Corregido

    def update(self):
        self.health_bar_group.update()
        self.icons_group.update()
        self.score_group.update()

    def draw(self, surface):
        self.health_bar_group.draw(surface)
        self.icons_group.draw(surface)
        self.score_group.draw(surface)  # Agregado para mostrar el score
