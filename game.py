import random
from time import sleep
import pygame
import pygame.locals
import winsound

# update_setting
clock = pygame.time.Clock()
FPS = 60

# init's
pygame.init()
pygame.font.init()

# define variables
array = []
sorted = False
red_column = 0
step = -1
max_step = 126
comparisions = 0
array_accesses = 0

# define font
WHITE = (255, 255, 255)
sys_font = pygame.font.SysFont("Fixedsys", 30)

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

def BubbleSort(unsorted_array, j):
    sort_array = unsorted_array 
    global step, max_step, comparisions, array_accesses, red_column
    if sort_array[j] > sort_array[j + 1]:
        sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
        array_accesses += 1

    if step >= max_step:
        max_step -= 1
        step = -1
    
    print(j)
    #(winsound.Beep(int(sort_array[j]) * + 37, 400)
    comparisions += 1
    red_column = j

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

    comparision_text = sys_font.render(f"Comparisions: {comparisions}", True, WHITE)
    screen.blit(comparision_text, (10, 10))
    array_accesses_text = sys_font.render(f"Array accesses: {array_accesses}", True, WHITE)
    screen.blit(array_accesses_text, (550, 10))
    delay_text = sys_font.render("Delay: 4 ms", True, WHITE)
    screen.blit(delay_text, (1170, 10))

    if(max_step != 0):
        print(max_step)
        print(step)
        step += 1
        BubbleSort(array, step)
        #sleep(0.004)
        DrawColumns(array)

    column_group.draw(screen)
    column_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass

    pygame.display.update()

if __name__ == "__main__":
    game_running = True