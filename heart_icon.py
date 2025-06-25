import pygame
import constants as c


class HeartIcon(pygame.sprite.Sprite):
    def __init__(self, x=20, y=None):
        super(HeartIcon, self).__init__()
        icon_size = (48, 48)  # Tamaño más grande para el icono
        self.img_heart_01 = pygame.transform.scale(
            pygame.image.load("heart_01.PNG").convert_alpha(), icon_size)
        self.img_heart_02 = pygame.transform.scale(
            pygame.image.load("heart_02.PNG").convert_alpha(), icon_size)
        self.img_heart_03 = pygame.transform.scale(
            pygame.image.load("heart_03.PNG").convert_alpha(), icon_size)
        self.img_heart_04 = pygame.transform.scale(
            pygame.image.load("heart_04.PNG").convert_alpha(), icon_size)
        self.img_heart_05 = pygame.transform.scale(
            pygame.image.load("heart_05.PNG").convert_alpha(), icon_size)
        self.anim_list = [
            self.img_heart_01,
            self.img_heart_02,
            self.img_heart_03,
            self.img_heart_04,
            self.img_heart_05]
        
        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 3
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        # Corrige el typo en el nombre de la constante
        display_height = c.DISPLAY_SIZE[1] if hasattr(c, "DISPLAY_SIZE") else 600
        if y is None:
            y = display_height - self.rect.height - 50
        self.rect.y = y

    def update(self):
        self.frame_duration -= 1
        if self.frame_duration <= 0:
            self.anim_index = (self.anim_index + 1) % len(self.anim_list)
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration

