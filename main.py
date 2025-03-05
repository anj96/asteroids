import pygame
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    pygame.init()
    clock = pygame.time.Clock()
    dt =0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # player1.update(dt)
        for thing in updatable:
            thing.update(dt)
        for object in  asteroids:
            if object.checkIfCollision(player1):
                print("Game over!")
                return 
        pygame.Surface.fill(screen, color=(0,0,0))
        for thing in drawable:
            thing.draw(screen)
        # player1.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()