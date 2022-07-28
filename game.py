from contextlib import redirect_stderr
import random
import pygame
import pygame.locals
from enum import Enum

# update_setting
clock = pygame.time.Clock()
FPS = 240

# init's
pygame.init()
pygame.font.init()

# define font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
sys_font = pygame.font.SysFont("Fixedsys", 30)

# size_screen
screen_width =  1500
screen_height = 700 

# screen_settings
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Ball Game")

# enum of sorting functions
class SortingFunctions(Enum):
    BubbleSort = 1
    ShakerSort = 2
    InsertionSort = 3
    ModBubbleSort = 4
    QuickSort = 5

# class Column
class Column(pygame.sprite.Sprite):
    def __init__(self, x, y, sizeX, sizeY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([sizeX, sizeY])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x, y]

#class button
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, sizeX, sizeY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([sizeX, sizeY])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x, y]

# define group
column_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()

# deifne methods
def CheckArray(unsorted_array):
    sort_array = unsorted_array
    checked = []
    for i in range(len(sort_array) - 1):
        checked.append(i)
        DrawingScreen(sort_array, [i], checked[:-1])

def Randomize():
    new_array = []
    for i in range(128):
        new_array.append(i + 1)
    for i in range(128):
        # randomed array
        index = random.randint(0, len(new_array) - 1)
        second_index = random.randint(0, len(new_array) - 1)
        new_array[index], new_array[second_index] = new_array[second_index], new_array[index]
        # sorted array
        # new_array[i] = i
    return new_array

def BinarySearch(sorted_array, elem, low, high):
    while low <= high:
        mid = (high + low) // 2
        if elem == sorted_array[mid]:
            return mid + 1
        elif elem > sorted_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        DrawingScreen(sorted_array, [elem], [mid])
    return low

def BubbleSort(unsorted_array):
    global sorted

    for i in range(len(unsorted_array) - 1):
        for j in range(len(unsorted_array) - 1 - i):
            if sorted == True:
                break
            if unsorted_array[j] > unsorted_array[j + 1]:
                unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]
                DrawingScreen(unsorted_array, [j], [j + 1])
    CheckArray(array)
    sorted = True

def ShakerSort(unsorted_array):
    left = 0
    right = len(unsorted_array) - 1

    global sorted

    while left <= right:
        for i in range(left, right, +1):
            if sorted == True:
                break
            if unsorted_array[i] > unsorted_array[i + 1]:
                unsorted_array[i], unsorted_array[i + 1] = unsorted_array[i + 1], unsorted_array[i]
                DrawingScreen(unsorted_array, [i], [i + 1])
        right -= 1
        for i in range(right, left, -1):
            if sorted == True:
                break
            if unsorted_array[i] < unsorted_array[i - 1]:
                unsorted_array[i], unsorted_array[i - 1] = unsorted_array[i - 1], unsorted_array[i]
                DrawingScreen(unsorted_array, [i], [i - 1])
        left += 1
    CheckArray(array)
    sorted = True

def InsertionSort(unsorted_array):
    global sorted

    for i in range(1, len(unsorted_array)):
        if sorted == True:
            break
        j = i - 1
        key = unsorted_array[i]
        loc = BinarySearch(unsorted_array, key, 0, j)
        while(j >= loc):
            unsorted_array[j + 1] = unsorted_array[j]
            j -= 1
            DrawingScreen(unsorted_array, [j], [loc])
        unsorted_array[j + 1] = key
    CheckArray(array)
    sorted = True

def ModBubbleSort(unsorted_array):
    sort_array = unsorted_array

    global sorted

    for i in range(0 ,(int(len(sort_array) / 2) - 1), +1):
        for j in range(1, len(sort_array) - 1 - i * 2, +1):
            if sorted == True:
                break
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
            if sort_array[j] < sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]
            DrawingScreen(sort_array, [j], [j + 1, j - 1])
    CheckArray(array)
    sorted = True

def QuickSort(unsorted_array):

    global sorted
    
    if unsorted_array == []:
        #CheckArray(unsorted_array)
        sorted = True
        return unsorted_array
    low = 0
    high = len(unsorted_array) - 1
    mid = (low + high) // 2
    if unsorted_array[mid] < unsorted_array[low]:
        unsorted_array[mid], unsorted_array[low] = unsorted_array[low], unsorted_array[mid]
    if unsorted_array[high] < unsorted_array[low]:
        unsorted_array[high], unsorted_array[low] = unsorted_array[low], unsorted_array[high]
    if unsorted_array[high] < unsorted_array[mid]:
        unsorted_array[high], unsorted_array[mid] = unsorted_array[mid], unsorted_array[high]
    pivot = unsorted_array.pop(mid)
    l_unsort_array = list(filter(lambda x: x <= pivot, unsorted_array))
    r_unsort_array = list(filter(lambda x: x > pivot, unsorted_array))
    DrawingScreen(unsorted_array, [pivot], [list(l_unsort_array + r_unsort_array)])
    #print(l_unsort_array + [pivot] + r_unsort_array)
    return list(QuickSort(l_unsort_array) + [pivot] + QuickSort(r_unsort_array))

def TextDraw():
    sort_text = sys_font.render("Bubble Sort", True, BLACK)
    screen.blit(sort_text, (15, 626))
    sort_text = sys_font.render("Shaker Sort", True, BLACK)
    screen.blit(sort_text, (155, 626))
    sort_text = sys_font.render("Binary Insertion Sort", True, BLACK)
    screen.blit(sort_text, (290, 626))
    sort_text = sys_font.render("Mod Bubble Sort", True, BLACK)
    screen.blit(sort_text, (512, 626))
    sort_text = sys_font.render("Quick sort (mediana)", True, BLACK)
    screen.blit(sort_text, (15, 666))

def DrawingScreen(drawed_array, red_array, green_array):
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    global column_group, button_group, array, game_running, sorted, selected_sort, start_sort, checked
    column_group = pygame.sprite.Group()
    offset = 0
    index = 0
    for elem in drawed_array:
        if list(green_array).count(index) > 0 :
            col = Column(offset + 45, screen_height - 100, 10, (elem + 1) * 4, (0, 255, 0))
        elif list(red_array).count(index) > 0 :
            col = Column(offset + 45, screen_height - 100, 10, (elem + 1) * 4, (255, 0, 0))
        else:
            col = Column(offset + 45, screen_height - 100, 10, (elem + 1) * 4, (255, 255, 255))
        column_group.add(col)
        offset += 11
        index += 1

    column_group.draw(screen)
    column_group.update()

    button_group.draw(screen)
    button_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sorted = True
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if button_group.sprites()[0].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                array = Randomize()
                selected_sort = SortingFunctions.BubbleSort
                sorted = False
            elif button_group.sprites()[0].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.BubbleSort
                sorted = True
            
            if button_group.sprites()[1].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                array = Randomize()
                selected_sort = SortingFunctions.ShakerSort
                sorted = False
            elif button_group.sprites()[1].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.ShakerSort
                sorted = True
            
            if button_group.sprites()[2].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                array = Randomize()
                selected_sort = SortingFunctions.InsertionSort
                sorted = False
            elif button_group.sprites()[2].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.InsertionSort
                sorted = True
            
            if button_group.sprites()[3].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                array = Randomize()
                selected_sort = SortingFunctions.ModBubbleSort
                sorted = False
            elif button_group.sprites()[3].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.ModBubbleSort
                sorted = True

            if button_group.sprites()[4].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                array = Randomize()
                selected_sort = SortingFunctions.QuickSort
                sorted = False
            elif button_group.sprites()[4].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.QuickSort
                sorted = True

    TextDraw()
    pygame.display.update()

# define variables
game_running = True
array = []
sorted = True
selected_sort = 'none'
array = Randomize()
checked = False

# start program
game_running = True
button_group.add(Button(10, 650, 128, 30))
button_group.add(Button(148, 650, 128, 30))
button_group.add(Button(282, 650, 220, 30))
button_group.add(Button(508, 650, 170, 30))
button_group.add(Button(10, 690, 215, 30))
#button_group.add(Button(10, 690, 100, 30, "Shaker Sort"))

while game_running:
    if selected_sort == SortingFunctions.BubbleSort and sorted == False:
        BubbleSort(array)
    elif selected_sort == SortingFunctions.ShakerSort and sorted == False:
        ShakerSort(array)
    elif selected_sort == SortingFunctions.InsertionSort and sorted == False:
        InsertionSort(array)
    elif selected_sort == SortingFunctions.ModBubbleSort and sorted == False:
        ModBubbleSort(array)
    elif selected_sort == SortingFunctions.QuickSort and sorted == False:
        QuickSort(array)
    else:
        DrawingScreen(array, [127], [0])

if __name__ == "__main__":
    game_running = True
