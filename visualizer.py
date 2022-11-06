import pygame, random, math
pygame.init()

class base:
    FONT = pygame.font.SysFont('Poppins', 50)
    BLACK = 40, 41, 40
    WHITE = 217, 212, 195
    SORTING_COLOUR = 212, 169, 121
    SIDE_PADDING = 120
    TOP_PADDING = 150

    def __init__(self, w, h, arr):
        self.width = w
        self.height = h
        self.window = pygame.display.set_mode((w, h)) 
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_arr(arr)

    def set_arr(self, arr):
        self.arr = arr
        self.minVal = min(arr)
        self.maxVal = max(arr)

        self.barWidth = round(self.width - self.SIDE_PADDING) / (2 * len(arr))
        self.barHeight = math.floor((self.height - self.TOP_PADDING) / (self.maxVal - self.minVal))
        self.startingX = self.SIDE_PADDING // 2

def draw(info):
    info.window.fill(info.BLACK)
    menu = info.FONT.render("R | S | A | D", 1, info.WHITE)
    algo = info.FONT.render("B | I | S | M | Q", 1, info.WHITE)

    info.window.blit(menu, (info.width/2 - menu.get_width()/2, 15))
    info.window.blit(algo, (info.width/2 - algo.get_width()/2, 60))

    drawBars(info, -1, -1)
    pygame.display.update()

def drawBars(info, a, b, c=-1, clr=False):
    arr = draw_info.arr

    if clr:
        rect = (draw_info.SIDE_PADDING//2, draw_info.TOP_PADDING, draw_info.width -
                draw_info.SIDE_PADDING, draw_info.height)
        pygame.draw.rect(draw_info.window, draw_info.BLACK, rect)

    for i, val in enumerate(arr):
        x = draw_info.startingX + (2 * i) * draw_info.barWidth
        y = draw_info.height - (val - draw_info.minVal +
                                1) * draw_info.barHeight
        colour = (217, 212, 195)
        if i == a or i == b or i == c:
            colour = draw_info.SORTING_COLOUR

        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.barWidth, draw_info.height))
    
    if clr:
        pygame.display.update()

def generateArray(n, minVal, maxVal):
    arr = []

    for i in range(n):
        arr.append(random.randint(minVal, maxVal))

    return arr

def bubbleSort(draw_info, ascending):
    lst = draw_info.arr
    clock = pygame.time.Clock()
    for i in range(len(arr)):
        for j in range(i + 1, len(lst)):
            clock.tick(100)
            if (ascending and lst[i] > lst[j]) or (not ascending and lst[i] < lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
            drawBars(draw_info, i, j, -1, True)

# ------- MAIN GAME LOOP -------
run = True
n = 30
minVal, maxVal = 0, 100

sorting = False
ascending = True
clock = pygame.time.Clock()

arr = generateArray(n, minVal, maxVal)
draw_info = base(1000, 800, arr)
algorithm = bubbleSort

while run:
    clock.tick(100)
    draw(draw_info)
    pygame.display.update()
    
    for event in pygame.event.get():
        # allows the user to close window
        if event.type == pygame.QUIT:
            run = False
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_r:
            arr = generateArray(n, minVal, maxVal)
            draw_info.set_arr(arr)
            sorting = False
        elif event.key == pygame.K_SPACE and sorting == False:
            sorting = True
            algorithm(draw_info, ascending)
        elif event.key == pygame.K_b and not sorting:
            algo = bubbleSort
            
   

pygame.quit()
