import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position ,radius=self.radius, width=2)
        
    
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(angle)
            vel_2 = self.velocity.rotate(-angle)
            smaller_rad = self.radius - ASTEROID_MIN_RADIUS 
            asteroid_1 = Asteroid(self.position.x, self.position.y, smaller_rad)
            asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_rad)
            asteroid_1.velocity = vel_1 * 1.2
            asteroid_2.velocity = vel_2 * 1.2
