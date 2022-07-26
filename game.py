from asyncio import start_server
from cgitb import text
import random
from time import sleep
from tokenize import group
from tracemalloc import start
import pygame
import pygame.locals
from enum import Enum

# update_setting
clock = pygame.time.Clock()
FPS = 60

# init's
pygame.init()
pygame.font.init()

# define font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
sys_font = pygame.font.SysFont("Fixedsys", 30)

# size_screen
screen_width =  1300 # 1024 for column size = 2, size_array = 256
screen_height = 700 # 256 for height column

# screen_settings
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Ball Game")

# enum of sorting functions
class SortingFunctions(Enum):
    BubbleSort = 1
    ShakerSort = 2

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
def Randomize():
    new_array = []
    for i in range(128):
        new_array.append(i + 1)
    for i in range(128):
        index = random.randint(0, 127)
        second_index = random.randint(0, 127)
        new_array[index], new_array[second_index] = new_array[second_index], new_array[index]
    return new_array

def BubbleSort(unsorted_array):
    sort_array = unsorted_array

    global sorted, comparisions, array_accesses, start_sort

    for i in range(len(sort_array) - 1):
        for j in range(len(sort_array) - 1 - i):
            if sorted == True:
                comparisions = 0
                array_accesses = 0
                break
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                array_accesses += 1
                DrawingScreen(sort_array, [j, j + 1])
            comparisions += 1
    start_sort = False
    sorted = True

def ShakerSort(unsorted_array):
    sort_array = unsorted_array
    left = 0
    right = len(sort_array) - 1

    global sorted, array_accesses, comparisions, start_sort

    while left <= right:
        for i in range(left, right, +1):
            if sorted == True:
                comparisions = 0
                array_accesses = 0
                break
            if sort_array[i] > sort_array[i + 1]:
                sort_array[i], sort_array[i + 1] = sort_array[i + 1], sort_array[i]
                array_accesses += 1
                DrawingScreen(sort_array, [i, i + 1])
            comparisions += 1
        right -= 1
        for i in range(right, left, -1):
            if sorted == True:
                array_accesses = 0
                comparisions = 0
                break
            if sort_array[i] < sort_array[i - 1]:
                sort_array[i], sort_array[i - 1] = sort_array[i - 1], sort_array[i]
                array_accesses += 1
                DrawingScreen(sort_array, [i, i - 1])
            comparisions += 1
            
        left += 1
    start_sort = False
    sorted = True

def TextDraw():
    comparision_text = sys_font.render(f"Comparisions: {comparisions}", True, WHITE)
    screen.blit(comparision_text, (10, 10))
    array_accesses_text = sys_font.render(f"Array accesses: {array_accesses}", True, WHITE)
    screen.blit(array_accesses_text, (550, 10))
    delay_text = sys_font.render("Delay: 4 ms", True, WHITE)
    screen.blit(delay_text, (1170, 10))
    sort_text = sys_font.render("Bubble Sort", True, BLACK)
    screen.blit(sort_text, (15, 626))

def DrawingScreen(drawed_array, red_array):
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    global column_group, button_group, array, game_running, sorted, selected_sort, start_sort
    column_group = pygame.sprite.Group()
    offset = 0
    index = 0
    for elem in drawed_array:
        if list(red_array).count(index) == 0 :
            col = Column(offset + 10, screen_height - 100, 8, elem * 4 + 2, (255, 255, 255))
        else:
            col = Column(offset + 10, screen_height - 100, 8, elem * 4 + 2, (255, 0, 0))
        column_group.add(col)
        offset += 10
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
                selected_sort = SortingFunctions.BubbleSort
                sorted = False
            elif button_group.sprites()[0].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.BubbleSort
                array = Randomize()
                print(len(array))
                sorted = True
            
            if button_group.sprites()[1].rect.collidepoint(pygame.mouse.get_pos()) and sorted == True:
                selected_sort = SortingFunctions.ShakerSort
                sorted = False
            elif button_group.sprites()[1].rect.collidepoint(pygame.mouse.get_pos()) and sorted == False:
                selected_sort = SortingFunctions.ShakerSort
                array = Randomize()
                sorted = True

    TextDraw()
    pygame.display.update()

# define variables
game_running = True
array = []
comparisions = 0
sorted = True
array_accesses = 0
selected_sort = 'none'
array = Randomize()

# start program
game_running = True
button_group.add(Button(10, 650, 128, 30))
button_group.add(Button(148, 650, 128, 30))
#button_group.add(Button(10, 690, 100, 30, "Shaker Sort"))

while game_running:
    if selected_sort == SortingFunctions.BubbleSort and sorted == False:
        BubbleSort(array)
    elif selected_sort == SortingFunctions.ShakerSort and sorted == False:
        ShakerSort(array)
    else:
        DrawingScreen(array, [0,127])

if __name__ == "__main__":
    game_running = True
