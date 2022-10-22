import pygame
import random
import math

pygame.init()

screenLength, screenHeight = 600, 300;
win = pygame.display.set_mode((screenLength, screenHeight)) 
pygame.display.set_caption("Sorting Algorithm Visualizer")


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        win.fill((0,0,0))
        clock.tick(100)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()