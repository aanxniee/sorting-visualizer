import pygame, random, math
pygame.init()

class base:
    FONT = pygame.font.SysFont('Poppins', 20)
    SIDE_PADDING = 120
    TOP_PADDING = 50

    def __init__(self, w, h, arr):
        self.width = w
        self.height = h
        self.window = pygame.display.set_mode((w, h)) 
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_arr(arr)

    def set_list(self, arr):
        self.arr = arr
        self.minVal = min(arr)
        self.maxVal = max(arr)

        self.barWidth = round(self.width - self.SIDE_PADDING) / (2 * len(arr))
        self.barHeight = math.floor((self.height - self.TOP_PADDING) / (self.maxVal - self.minVal))
        self.startingX = self.SIDE_PADDING // 2


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
