from util import print_array
from random import randint
import time as t

def mergesort(array):
    length = len(array)

    if length < 2:
        return
    mid = (int) (length / 2)
    left = [ array[i] for i in range(mid) ]
    right = [ array[i] for i in range(mid, length) ]

    mergesort(left)
    mergesort(right)
    merge(array, left, right)


def merge(array, left, right):
    left_size = len(left)
    right_size = len(right)
    i, j, k = 0, 0, 0

    while i < left_size and j < right_size:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while i < left_size:
        array[k] = left[i]
        i, k = i + 1, k + 1
    while j < right_size:
        array[k] = right[j]
        j, k = j + 1, k + 1


if __name__ == '__main__':
    time = t.time()
    numbers = []

    for i in range(10):
        numbers.append(randint(0, 100))
    print("Before : ")
    print(numbers)

    mergesort(numbers)

    print("After : ")
    print(numbers)

    time = round(t.time() - time, 6)
    print(f"Program finished in {time} seconds")
