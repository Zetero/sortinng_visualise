import random
from time import sleep
array = []

def Randomize():
    for i in range(128):
        array.append(i + 1)
    for i in range(128):
        index = random.randint(0, 127)
        second_index = random.randint(0, 127)
        array[index], array[second_index] = array[second_index], array[index]
    return array

def BubbleSort():
    sort_array = Randomize()
    print(sort_array)
    for i in range(len(sort_array) - 1):
        for j in range(len(sort_array) - 1 - i):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
    print(sort_array)

if __name__ == "__main__":
    BubbleSort()