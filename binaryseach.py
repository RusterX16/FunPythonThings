from random import randint
import time as t

from .quicksort import quicksort

def binarysearch(array, element, left, right):
    if(left > right):
        return -1
    mid = int(left + ((right - left) / 2))

    if(array[mid] == element):
        return mid;
    elif(array[mid] > element):
        return binarysearch(array, element, left, mid - 1)
    else:
        return binarysearch(array, element, mid + 1, right)


if __name__ == '__main__':
    time = t.time()
    numbers = [ i**2 for i in range(10) ]
    element = 9

    index = binarysearch(numbers, element, 0, len(numbers) - 1)
    quicksort(numbers, 0, len(numbers) - 1)

    print(f"{element} found at index {index}")

    time = round(t.time() - time, 6)
    print(f"Program finished in {time} seconds")