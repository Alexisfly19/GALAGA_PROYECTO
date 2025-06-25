import pygame
import math

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed=7):
        super().__init__()
        # Usa una imagen personalizada
        self.image = pygame.image.load("enemy_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (24, 48))  # Ahora la bala es más grande
        self.rect = self.image.get_rect(center=(x, y))
        # Calcular dirección hacia el objetivo
        dx = target_x - x
        dy = target_y - y
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1  # Evita división por cero
        self.vel_x = speed * dx / dist
        self.vel_y = speed * dy / dist

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Elimina la bala si sale de la pantalla
        if self.rect.y > 800 or self.rect.y < -20 or self.rect.x < -20 or self.rect.x > 1200:
            self.kill()