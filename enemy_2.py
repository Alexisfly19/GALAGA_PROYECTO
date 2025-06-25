import pygame
import constants as c
import random
from enemy_bullet import EnemyBullet


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()

        enemy_size = 100  # o el tamaño real de tu enemigo
        explosion_size = int(enemy_size * 1.2)  # 20% más grande que el enemigo

        self.img_explosion_01 = pygame.image.load("explosion_01.PNG").convert_alpha()
        self.img_explosion_01 = pygame.transform.scale(self.img_explosion_01, (explosion_size, explosion_size))
        
        self.img_explosion_02 = pygame.image.load("explosion_02.PNG").convert_alpha()
        self.img_explosion_02 = pygame.transform.scale(self.img_explosion_02, (explosion_size, explosion_size))
        
        self.img_explosion_03 = pygame.image.load("explosion_03.PNG").convert_alpha()
        self.img_explosion_03 = pygame.transform.scale(self.img_explosion_03, (explosion_size, explosion_size))
        
        self.img_explosion_04 = pygame.image.load("explosion_04.PNG").convert_alpha()
        self.img_explosion_04 = pygame.transform.scale(self.img_explosion_04, (explosion_size, explosion_size))
        
        self.img_explosion_05 = pygame.image.load("explosion_05.PNG").convert_alpha()
        self.img_explosion_05 = pygame.transform.scale(self.img_explosion_05, (explosion_size, explosion_size))



        self.anim_explosion = [self.img_explosion_01, self.img_explosion_02, self.img_explosion_03,
                                    self.img_explosion_04, self.img_explosion_05]
        self.anim_index = 0
        self.frame_length = 3
        self.image = pygame.image.load("enemy_2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))# Ajusta el tamaño del enemigo
        self.is_destroyed = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound("snd_hit_01.ogg")


        self.hp = 5  # Puntos de vida del enemigo
        self.snd_hit.set_volume(0.5)  # Ajusta el

        self.bullets = pygame.sprite.Group()  # Grupo para las balas del enemigo
        self.bullet_timer_max = 60
        self.bullet_timer = self.bullet_timer_max  # Temporizador para disparar balas
        self.states = {'FLY_DOWN': 'FLY_DOWN', 'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True


        self.score_value = 250  # Valor de puntos al destruir el enemigo
        self.vel_x = 0
        self.vel_y = 3  # <--- Cambia este valor para la velocidad vertical inicial


    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= 200:
            self.state = self.states['ATTACK']
            self.init_state = True

    def state_attack(self):
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = 1  # <--- Cambia estos valores para la velocidad horizontal
            self.init_state = False
        if self.rect.x <= 0:
            self.vel_x *= -1
        elif self.rect.x + self.rect.width >= c.DISPAY_WIDTH:
            self.vel_x *= -1


    def get_hit(self):
        self.snd_hit.play()
        self.hp -= 1
        print("Enemy hit! Remaining HP:", self.hp)
        if self.hp <= 0:
            self.is_destroyed = True
            # Centra la explosión en la posición actual del enemigo
            self.anim_index = 0
            self.frame_length = 3
            # Ajusta el rect para la animación de explosión
            self.rect = self.anim_explosion[0].get_rect(center=self.rect.center)

    def update(self, ship=None):
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
            self.state_attack()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Disparo hacia el ship
        if self.state == 'ATTACK' and ship is not None:
            self.bullet_timer -= 1
            if self.bullet_timer <= 0:
                bullet = EnemyBullet(
                    self.rect.centerx,
                    self.rect.bottom,
                    ship.rect.centerx,
                    ship.rect.centery
                )
                self.bullets.add(bullet)
                self.bullet_timer = self.bullet_timer_max

        self.bullets.update()

        if self.is_destroyed:
            max_index = len(self.anim_explosion) - 1
            if self.anim_index > max_index:
                self.kill()
            else:
                if self.frame_length == 0:
                    self.image = self.anim_explosion[self.anim_index]
                    self.rect = self.image.get_rect(center=self.rect.center)
                    self.anim_index += 1
                    self.frame_length = 3
                else:
                    self.frame_length -= 1

