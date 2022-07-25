import random
from time import sleep
import pygame
import pygame.locals

# update_setting
clock = pygame.time.Clock()
FPS = 60

# define variables
array = []
sorted = False
red_column = 0

# size_screen
screen_width =  1300 # 1024 for column size = 2, size_array = 256
screen_height = 700 # 256 for height column

# screen_settings
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Ball Game")

# class Column
class Column(pygame.sprite.Sprite):
    def __init__(self, x, y, sizeX, sizeY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([sizeX, sizeY])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x, y]
    
    def update(self):
        pass
        #self.rect.y += 1

# define group
column_group = pygame.sprite.Group()

# deifne methods
def Randomize():
    for i in range(128):
        array.append(i + 1)
    for i in range(128):
        index = random.randint(0, 127)
        second_index = random.randint(0, 127)
        array[index], array[second_index] = array[second_index], array[index]
    return array

def BubbleSort(unsorted_array):
    sort_array = unsorted_array 
    for i in range(len(sort_array) - 1):
        for j in range(len(sort_array) - 1 - i):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                
                global red_column
                red_column = j
                break

def DrawColumns(drawed_array):
    global column_group
    column_group = pygame.sprite.Group()
    array = drawed_array
    offset = 0
    index = 0
    global red_column
    for elem in array:
        if index != red_column and index != red_column + 1:
            col = Column(offset + 10, screen_height - 100, 8, elem * 4 + 2, (255, 255, 255))
        else:
            col = Column(offset + 10, screen_height - 100, 8, elem * 4 + 2, (255, 0, 0))
        column_group.add(col)
        offset += 10
        index += 1


array = Randomize()
DrawColumns(array)

game_running = True
while game_running:

    clock.tick(FPS)

    screen.fill((0, 0, 0))

    column_group.draw(screen)
    column_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                BubbleSort(array)
                DrawColumns(array)

    pygame.display.update()

if __name__ == "__main__":
    game_running = True