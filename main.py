import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    dt = 0

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()


    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    Shot.containers = (shots, updatable, drawable)
    

    while True:

        # enable close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        updatable.update(dt)
        
        # player/asteroid collision check
        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Game over!")
                sys.exit()

        # shot/asteroid collision check
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.kill()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # FPS limit = 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
