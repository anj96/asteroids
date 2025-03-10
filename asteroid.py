from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from random import uniform
import pygame

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x,self.position.y), self.radius,2)

    def update(self, dt):
        self.position += self.velocity*dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = uniform(20,50)
        velocity_1=pygame.Vector2(self.position.x, self.position.y).rotate(angle)
        velocity_2=pygame.Vector2(self.position.x, self.position.y).rotate(-angle)
        new_radius=self.radius - ASTEROID_MIN_RADIUS
        asteroid1= Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2= Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity=velocity_1
        asteroid2.velocity=velocity_2