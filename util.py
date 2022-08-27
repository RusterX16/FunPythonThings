def swap(array, val1, val2):
    array[val1], array[val2] = array[val2], array[val1]


def print_array(array):
    out = "["

    for i, val in enumerate(array):
        separator = ", "

        if i == len(array) - 1:
            separator = ""
        out += f"{val}{separator}"
    print(f"{out}]")