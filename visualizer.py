import pygame, random, math
pygame.init()

# class that initializes the pygame GUI
class base:
    # constants
    FONT = pygame.font.SysFont('Poppins', 30)
    BLACK = 40, 41, 40
    WHITE = 217, 212, 195
    SORTING_COLOUR = 212, 169, 121
    SIDE_PADDING = 120
    TOP_PADDING = 150

    # sets the window dimensions
    def __init__(self, w, h, arr):
        self.width = w
        self.height = h
        self.window = pygame.display.set_mode((w, h)) 
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_arr(arr)

    # sets the bars to be sorted
    def set_arr(self, arr):
        self.arr = arr
        self.minVal = min(arr)
        self.maxVal = max(arr)

        # dimensions for each bar depending on the random number generated
        self.barWidth = round(self.width - self.SIDE_PADDING) / (2 * len(arr))
        self.barHeight = math.floor((self.height - self.TOP_PADDING) / (self.maxVal - self.minVal))
        self.startingX = self.SIDE_PADDING // 2

 # function that draws to the window
def draw(draw_info):
    draw_info.window.fill(draw_info.BLACK)

    # display sorting options
    menu = draw_info.FONT.render("R (reset) | S (sort) | A (ascending) | D (descending", 1, draw_info.WHITE)
    algo = draw_info.FONT.render("B (bubble) | I (insertion) | S (selection) | M (merge) | Q (quick)", 1, draw_info.WHITE)
    draw_info.window.blit(menu, (draw_info.width/2 - menu.get_width()/2, 25))
    draw_info.window.blit(algo, (draw_info.width/2 - algo.get_width()/2, 50))

    drawBars(draw_info, -1, -1) # calls the drawBars function
    pygame.display.update()

# function that draws bars
def drawBars(draw_info, a, b, c = -1, clr = False):
    arr = draw_info.arr # set the array

    if clr:
        # create a bar for each "number" to be sorted
        rect = (draw_info.SIDE_PADDING//2, draw_info.TOP_PADDING, draw_info.width -
                draw_info.SIDE_PADDING, draw_info.height)
        pygame.draw.rect(draw_info.window, draw_info.BLACK, rect)

    # convert each number in the array to a bar
    for i, val in enumerate(arr):
        x = draw_info.startingX + (2 * i) * draw_info.barWidth
        y = draw_info.height - (val - draw_info.minVal +
                                1) * draw_info.barHeight
        colour = (217, 212, 195)
        # while the bar is being checked, change the colour (to show it is being iterated over)
        if i == a or i == b or i == c:
            colour = draw_info.SORTING_COLOUR

        # draw each bar
        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.barWidth, draw_info.height))
    
    if clr:
        pygame.display.update()

# function that generates the array of numbers to be sorted
def generateArray(n, minVal, maxVal):
    arr = []

    for i in range(n):
        arr.append(random.randint(minVal, maxVal))

    return arr

# bubble sort algorithm
def bubbleSort(draw_info, ascending):
    arr = draw_info.arr # initialize array
    clock = pygame.time.Clock()

    # traverse through the input array and compare adjacent elements
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            clock.tick(150)
            if (ascending and arr[i] > arr[j]) or (not ascending and arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i] # swap adjacent elements
            drawBars(draw_info, i, j, -1, True)

# insertion sort algorithm
def insertionSort(draw_info, ascending):
    arr = draw_info.arr # initialize array
    clock = pygame.time.Clock()

    # iterate through the array
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            clock.tick(50)
            # compare the current element to the element before it (predecessor)
            # if it is smaller, compare it to the element before that
            # move larger elements one index up by swapping
            if (ascending and arr[j] < arr[j - 1]) or (not ascending and arr[j] > arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            drawBars(draw_info, j, j - 1, -1, True)

# selection sort algorithm
def selectionSort(draw_info, ascending):
    arr = draw_info.arr # initalize array
    clock = pygame.time.Clock()

    index = 0 # initialize minimum value to location 0

    # traverse through array to find minimum value
    for i in range(len(arr)):
        index = i # set index of siu
        for j in range(i, len(arr)):
            clock.tick(150)
            # if any element is smaller than the element at index, swap the values
            if (ascending and arr[j] < arr[index]) or (not ascending and arr[j] > arr[index]):
                index = j # update the index of the minimum value
            drawBars(draw_info, index, j, -1, True)
        arr[i], arr[index] = arr[index], arr[i]

# quick sort algorithm
def quickSort(draw_info, ascending):
    quickSortHelper(draw_info, ascending, 0, len(draw_info.arr))

# function to find the partition position
def quickSortHelper(draw_info, ascending, start, end):
    arr = draw_info.arr # initialize array 

    if end <= start:
        return

    pos = end - 1 # pointer for the greater element
    clock = pygame.time.Clock()

    # traverse through all elements and compare each element with pivot
    for i in range(end - 1, start, -1):
        clock.tick(150)

        # if element smaller than the pivot is found, swap it with the greater element pointed
        if (ascending and arr[i] > arr[start]) or (not ascending and arr[i] < arr[start]):
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -= 1
        drawBars(draw_info, start, i, pos, True)
        arr[pos], arr[start] = arr[start], arr[pos]

    quickSortHelper(draw_info, ascending, start, pos) # recursive call to the left of pivot
    quickSortHelper(draw_info, ascending, pos + 1, end) # recursive call to the right of pivot

# merge sort algorithm (merging the two halves)
def merge(draw_info, arr, l, r, ascending):
    i = j = 0
    clock = pygame.time.Clock()

    for pos in range(len(l)+len(r)):
        clock.tick(100)
        temp = arr # copy data to temp array
        p1 = p2 = -1
        list1=True

        # find smaller element
        if i == len(l) or (j < len(r) and ((ascending and r[j] < l[i]) or (not ascending and r[j] > l[i]))):
            arr[pos] = l[j]
            j += 1
            list1 = False
        else:
            arr[pos] = l[i]
            i += 1

        for k in range(len(arr)):
            if arr[k] != temp[k]:
                if p1 == -1:
                    p1 = k
                else:
                    p2 = k

        drawBars(draw_info, p1, p2, -1, True)

        if list1:
            i += 1
        else:
            j += 1

    return arr

# merge sort algorithm (merging the two halves)
# overloaded with extra parameter
def merge(draw_info, arr, l, r, ascending, start):
    i = j = 0
    clock = pygame.time.Clock()
    for pos in range(len(l) + len(r)):
        clock.tick(150)
        # find smaller element
        if i == len(l) or (j < len(r) and ((ascending and r[j] < l[i]) or (not ascending and r[j] > l[i]))):
            arr[pos] = r[j]
            j += 1
            drawBars(draw_info, pos + start, len(l) + start + j, -1, True)
        else:
            arr[pos] = l[i]
            drawBars(draw_info, pos + start, start + i, -1, True)
            i += 1

    return arr

def mergeSort(draw_info, ascending):
    mergeSortHelper(draw_info, draw_info.arr, ascending, 0)

# function that splits the array into 2 halves and then remerges them
def mergeSortHelper(draw_info, arr, ascending, start):
    if len(arr) == 1:
        return

    # finds the mid index of the array
    mid = len(arr) // 2

    # divides array into 2 halves
    l = arr[:mid]
    r = arr[mid:]

    mergeSortHelper(draw_info, l, ascending, start) # sort first half
    mergeSortHelper(draw_info, r, ascending, start + len(arr) // 2) # sort second half
    arr = merge(draw_info, arr, l, r, ascending, start) # merge the two halves

# ------- MAIN GAME LOOP -------
run = True
n = 40
minVal, maxVal = 0, 100

sorting = False
ascending = True
clock = pygame.time.Clock()

arr = generateArray(n, minVal, maxVal) # generate array using method
draw_info = base(1000, 800, arr) # initialize window settings
algorithm = bubbleSort

while run:
    clock.tick(120)
    draw(draw_info)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allows the user to close window
            run = False
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_r: # reset key, generate new unsorted array
            arr = generateArray(n, minVal, maxVal)
            draw_info.set_arr(arr)
            sorting = False
        elif event.key == pygame.K_SPACE and sorting == False: # allows user to sort
            sorting = True
            algorithm(draw_info, ascending)

        # allows user to pick between ascending and descending
        elif event.key == pygame.K_a and not sorting:
            ascending = True
        elif event.key == pygame.K_d and not sorting:
            ascending = False
        
        # allows user to pick the sort algorithm (bubble, selection, insertion, quick, merge)
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
