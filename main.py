import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  player = Player(x, y, PLAYER_RADIUS)
  Shot.containers = (shots, drawable, updatable)

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill("black")
    for item in drawable:
       item.draw(screen)
    for item in updatable:
       item.update(dt)
    for asteroid in asteroids:
        if asteroid.check_collision(player):
           print("Game over!")
           sys.exit()

        for shot in shots:
           if asteroid.check_collision(shot):
              asteroid.split()
              shot.kill()
              
    pygame.display.flip()
    time_passed = clock.tick(60)
    dt = time_passed / 1000

if __name__ == "__main__":
    main()