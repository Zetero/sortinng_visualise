import random
import time
array = []

def Randomize():
    for i in range(128):
        array.append(i + 1)
    for i in range(128):
        index = random.randint(0, 127)
        second_index = random.randint(0, 127)
        array[index], array[second_index] = array[second_index], array[index]
    return array

def BubbleSort(new_array):
    start_time = time.time()

    sort_array = new_array
    for i in range(len(sort_array) - 1):
        for j in range(len(sort_array) - 1 - i):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
    
    print(f"Elapsed time: {abs(start_time - time.time())} sec")

def ModBubbleSort(new_array):
    start_time = time.time()

    sort_array = new_array
    for i in range(0 , int(len(sort_array) / 2) - 1, +1):
        for j in range(1, len(sort_array) - 1 - i * 2, +1):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
            if sort_array[j] < sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]

    print(f"Elapsed time: {abs(start_time - time.time())} sec")

def ShakerSort():
    sort_array = Randomize()
    print(sort_array)
    left = 0
    right = len(sort_array) - 1
    while left <= right:
        for i in range(left, right, +1):
            if sort_array[i] > sort_array[i + 1]:
                sort_array[i], sort_array[i + 1] = sort_array[i + 1], sort_array[i]
        right -= 1

        for i in range(right, left, -1):
            if sort_array[i] < sort_array[i - 1]:
                sort_array[i], sort_array[i - 1] = sort_array[i - 1], sort_array[i]
        left += 1
    print(sort_array)

def InsertionSort():
    sort_array = Randomize()
    for i in range(1, len(sort_array), +1):
        key = sort_array[i]
        j = i - 1
        while j > 0 and sort_array[j] < key:
            sort_array[j + 1] = sort_array[j]
            j -= 1
        sort_array[j + 1] = key

if __name__ == "__main__":
    first_array = Randomize()
    print("--bubble sort--")
    BubbleSort(first_array.copy())
    print("--mod bubble sort--")
    ModBubbleSort(first_array.copy())

    