import pygame, random, math

pygame.init()

screenLength, screenHeight = 600, 300;
win = pygame.display.set_mode((screenLength, screenHeight)) 
pygame.display.set_caption("Sorting Algorithm Visualizer")

clock = pygame.time.Clock()

# ------- MAIN GAME LOOP -------
run = True

while run:
    win.fill((0,0,0))

    for event in pygame.event.get():
        # allows the user to close window
        if event.type == pygame.QUIT:
            run = False

    clock.tick(50)
    pygame.display.update()

pygame.quit()
