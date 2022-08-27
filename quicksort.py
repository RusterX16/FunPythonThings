from util import swap
from random import randint
import time as t


def quicksort(array, start, end):
    if start >= end:
        return

    pivot = array[end]
    left = start
    right = end

    while left < right:
        while array[left] <= pivot and left < right:
            left += 1
        while array[right] >= pivot and left < right:
            right -= 1
        swap(array, left, right)
    swap(array, left, end)
    quicksort(array, start, left - 1)
    quicksort(array, left + 1, end)


if __name__ == '__main__':
    time = t.time()
    numbers = [ randint(0, 100) for _ in range(10) ]

    print(f"Before : \n{numbers}")
    quicksort(numbers, 0, len(numbers) - 1)
    print(f"After : \n{numbers}")

    time = round(t.time() - time, 6)
    print(f"Program finished in {time} seconds")