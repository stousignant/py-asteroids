from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
import sys

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatables, drawables)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for element in drawables:
            element.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for element in updatables:
            element.update(dt)
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                sys.exit(0)


if __name__ == "__main__":
    main()
