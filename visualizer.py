import pygame, random, math

pygame.init()

screenLength, screenHeight = 600, 300;
win = pygame.display.set_mode((screenLength, screenHeight)) 
pygame.display.set_caption("Sorting Algorithm Visualizer")

clock = pygame.time.Clock()


def generateArray(n, minVal, maxVal):
    arr = []

    for i in range(n):
        arr.append(random.randint(minVal, maxVal))

    return arr

# ------- MAIN GAME LOOP -------
run = True
n = 20
minVal, maxVal = 0, 100

sorting = False
ascending = True

arr = generateArray(n, minVal, maxVal)

while run:
    win.fill((0,0,0))

    for event in pygame.event.get():
        # allows the user to close window
        if event.type == pygame.QUIT:
            run = False

    clock.tick(50)
    pygame.display.update()

pygame.quit()
