from random import randint
from util import swap
import time as t


def selectionsort(array):
    for i in range(len(array) - 1):
        i_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[i_min]:
                i_min = j
        swap(array, i, i_min)


if __name__ == '__main__':
    time = t.time()
    numbers = [ randint(0, 100) for _ in range(10) ]

    print(f"Before : \n{numbers}")
    selectionsort(numbers)
    print(f"After : \n{numbers}")

    time = round(t.time() - time, 6)
    print(f"Program finished in {time} seconds")