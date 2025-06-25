import pygame
import constants as c
from bullet import Bullet
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self,):
        super(Ship, self).__init__()
        self.image_normal = pygame.transform.scale(
            pygame.image.load("ship.png").convert_alpha(), (50, 50))
        self.image_invincible = pygame.transform.scale(
            pygame.image.load("ship_invincible.png").convert_alpha(), (50, 50)) 
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPAY_WIDTH//2
        self.rect.y = c.DISPAY_HEIGHT - self.rect.height * 3
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound("snd_bullet_01.ogg")
        
        self.max_hp = 7 # Puntos de vida máximos
        self.lives = 3 # Vidas del jugador
        self.hp = self.max_hp
        self.hud = HUD(self.hp, self.lives) 
        self.hud.health_bar.rect.x = 20  # Margen izquierdo
        self.hud.health_bar.rect.y = c.DISPLAY_SIZE[1] - self.hud.health_bar.rect.height - 10  # Margen inferior
        
        self.is_invincible = False 
        self.max_invincible_timer = 120  # 2 segundos a 60 FPS
        self.invincible_timer = 0 # Temporizador de invulnerabilidad

        self.vel_x = 0 
        self.vel_y = 0 
        self.speed = 5


    def update(self):
        self.bullets.update() # Actualiza las balas
        self.hud.health_bar_group.update()  # Actualiza la barra de vida
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPAY_WIDTH - self.rect.width: 
            self.rect.x = c.DISPAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y

        # check for invincibility
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            self.is_invincible = True
            self.image = self.image_invincible  # Cambio de imagen al estado invencible
        else:
            self.is_invincible = False
            self.image = self.image_normal  # Vuelve a la imagen original
        print(self.is_invincible)


    def shoot(self):
        self.snd_shoot.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 4 
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)


    def get_hit(self):
        self.hp -= 1
        self.hud.health_bar.decrease_hp_value()
        if self.hp <= 0:
            self.hp
            self.death()
        print("Ship hit! Remaining HP:", self.hp)

    def death(self):
        self.lives -= 1
        print(f"Lives remaining: {self.lives}")
        if self.lives <= 0:
            self.lives = 0
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        print("Ship destroyed! Resetting HP")
        self.hud.lives.decrement_lives()
        self.rect.x = c.DISPAY_WIDTH // 2  # Reset position to center
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer


