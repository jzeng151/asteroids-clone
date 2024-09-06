import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)

  def draw(self, screen):
    width = 2
    color = "white"
    pygame.draw.circle(screen, color, self.position, self.radius, width)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self, ):
    self.kill()
    if self.radius < ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(20, 50)
    split_vec_1 = self.velocity.rotate(angle)
    split_vec_2 = self.velocity.rotate(-angle)
    
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
    new_asteroid_1.velocity = split_vec_1 * 1.2
    new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
    new_asteroid_2.velocity = split_vec_2 * 1.2
