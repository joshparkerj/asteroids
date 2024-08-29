# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print( "Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(player.radius)
    while True:
        screen.fill("#000000")
        # draw things each frame
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # This method should be called once per frame.
        # It will compute how many milliseconds have passed since the previous call.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
