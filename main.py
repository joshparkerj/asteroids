# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print( "Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    game_on = True
    while game_on:
        screen.fill("#000000")
        # draw things each frame
        for spr in drawable:
            spr.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # This method should be called once per frame.
        # It will compute how many milliseconds have passed since the previous call.
        dt = clock.tick(60) / 1000
        for spr in updatable:
            spr.update(dt)
        for spr in asteroids:
            if spr.is_colliding(player):
                print("GAME OVER!")
                game_on = False
            for bullet in bullets:
                if spr.is_colliding(bullet):
                    spr.split()
                    bullet.kill()


if __name__ == "__main__":
    main()
