from random import randint
from util import swap
import time as t


def bubblesort(array):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                swapped = True


if __name__ == '__main__':
    time = t.time()
    numbers = [ randint(0, 100) for _ in range(10) ]

    print(f"Before :\n{numbers}")
    bubblesort(numbers)
    print(f"After :\n{numbers}")

    time = round(t.time() - time, 6)
    print(f"Program finished in {time} seconds")