import pygame
from particle import Particle
import random



class ParticleSpawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()
    

    def update(self):
        self.particle_group.update()


    def spawn_particle(self, pos):
        random_number = random.randrange(3, 30)
        for num_particle in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = pos[0]
            new_particle.rect.y = pos[1]
            self.particle_group.add(new_particle)