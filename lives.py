import pygame
import constants as c


class Lives(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super().__init__()
        self.num_lives = num_lives
        self.width = 120
        self.height = 40
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)  # Permite transparencia
        self.ship_image = pygame.image.load("ship.png").convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (32, 32))  # Tamaño fijo
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)
        self.font_color = (255, 255, 255)
        self.rect = self.image.get_rect()
        self.vel_x  = 0
        self.vel_y = 0
        self.update()  # Dibuja la imagen y el texto inicial

    def update(self):
        self.image.fill((0, 0, 0, 0))  # Limpia el Surface con transparencia
        self.image.blit(self.ship_image, (0, 4))  # Dibuja el ícono de la nave
        lives_counter = self.font.render(f"x {self.num_lives}", True, self.font_color)
        self.image.blit(lives_counter, (40, 8))  # Dibuja el contador al lado

    def decrement_lives(self):
        self.num_lives -= 1
        if self.num_lives < 0:
            self.num_lives = 0
            
        self.update()  # Solo esto es suficiente

