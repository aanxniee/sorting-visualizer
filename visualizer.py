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
    arr = draw_info.arr
    clock = pygame.time.Clock()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            clock.tick(150)
            if (ascending and arr[i] > arr[j]) or (not ascending and arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            drawBars(draw_info, i, j, -1, True)

def insertionSort(draw_info, ascending):
    arr = draw_info.arr
    clock = pygame.time.Clock()
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            clock.tick(50)
            if (ascending and arr[j] < arr[j - 1]) or (not ascending and arr[j] > arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            drawBars(draw_info, j, j - 1, -1, True)

def selectionSort(draw_info, ascending):
    arr = draw_info.arr
    clock = pygame.time.Clock()
    idx = 0
    for i in range(len(arr)):
        idx = i
        for j in range(i, len(arr)):
            clock.tick(150)
            if (ascending and arr[j] < arr[idx]) or (not ascending and arr[j] > arr[idx]):
                idx = j
            drawBars(draw_info, idx, j, -1, True)
        arr[i], arr[idx] = arr[idx], arr[i]

def quickSort(draw_info, ascending):
    quickSortRange(draw_info, ascending, 0, len(draw_info.arr))

def quickSortRange(draw_info, ascending, start, end):
    arr = draw_info.arr

    if end<= start:
        return

    pos = end-1
    clock =pygame.time.Clock()
    for i in range(end-1, start, -1):
        clock.tick(150)
        if (ascending and arr[i]>arr[start]) or (not ascending and arr[i] < arr[start]):
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -=1
        drawBars(draw_info, start, i, pos, True)
        arr[pos], arr[start] = arr[start], arr[pos]
    quickSortRange(draw_info, ascending, start, pos)
    quickSortRange(draw_info, ascending, pos + 1, end)

def merge(draw_info, arr, arr1, arr2, ascending):
    x1 = x2 =0
    clock = pygame.time.Clock()
    for pos in range(len(arr1)+len(arr2)):
        clock.tick(100)
        temp = arr
        p1=p2=-1
        list1=True
        if x1 == len(arr1) or (x2 < len(arr2) and ((ascending and arr2[x2] < arr1[x1]) or (not ascending and arr2[x2] > arr1[x1]))):
            arr[pos] = arr2[x2]
            x2 += 1
            list1 = False
        else:
            arr[pos] = arr1[x1]
            x1 += 1
        for i in range(len(arr)):
            if arr[i] != temp[i]:
                if p1 == -1:
                    p1 = i
                else:
                    p2 = i
        drawBars(draw_info, p1, p2, -1, True)
        if list1:
            x1 += 1
        else:
            x2 += 1
    return arr

def merge(draw_info, arr, arr1, arr2, ascending, start):
    x1 = x2 = 0
    frames = pygame.time.Clock()
    for pos in range(len(arr1) + len(arr2)):
        frames.tick(150)
        if x1 == len(arr1) or (x2 < len(arr2) and ((ascending and arr2[x2] < arr1[x1]) or (not ascending and arr2[x2] > arr1[x1]))):
            arr[pos] = arr2[x2]
            x2 += 1
            drawBars(draw_info, pos + start, len(arr1) + start + x2, -1, True)
        else:
            arr[pos] = arr1[x1]
            drawBars(draw_info, pos + start, start + x1, -1, True)
            x1 += 1
    return arr

def mergeSort(draw_info, ascending):
    mergeSortHelper(draw_info, draw_info.arr, ascending, 0)

def mergeSortHelper(draw_info, arr, ascending, start):
    if len(arr) == 1:
        return
    left = len(arr) // 2
    right = len(arr) - left
    left_list = []
    right_list = []
    for i in range(left):
        left_list.append(arr[i])
    for i in range(right):
        right_list.append(arr[i + left])
    mergeSortHelper(draw_info, left_list, ascending, start)
    mergeSortHelper(draw_info, right_list, ascending, start + len(arr) // 2)
    arr = merge(draw_info, arr, left_list, right_list, ascending, start)

# ------- MAIN GAME LOOP -------
run = True
n = 40
minVal, maxVal = 0, 100

sorting = False
ascending = True
clock = pygame.time.Clock()

arr = generateArray(n, minVal, maxVal)
draw_info = base(1000, 800, arr)
algorithm = bubbleSort

while run:
    clock.tick(120)
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
        elif event.key == pygame.K_a and not sorting:
            ascending = True
        elif event.key == pygame.K_d and not sorting:
            ascending = False
        elif event.key == pygame.K_b and not sorting:
            algorithm = bubbleSort
        elif event.key == pygame.K_i and not sorting:
            algorithm = insertionSort
        elif event.key == pygame.K_s and not sorting:
            algorithm = selectionSort
        elif event.key == pygame.K_q and not sorting:
            algorithm = quickSort
        elif event.key == pygame.K_m and not sorting:
            algorithm = mergeSort
            
pygame.quit()
