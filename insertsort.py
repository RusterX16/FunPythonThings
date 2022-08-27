from random import randint
import time as t


def insertsort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1

        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current


if __name__ == '__main__':
    time = t.time()
    numbers = [ randint(0, 100) for _ in range(10) ]

    print(f"Before :\n{numbers}")
    insertsort(numbers)
    print(f"After : \n{numbers}")

    time = round(t.time() - time, 6)
    print(f"Program finish in {time} seconds")