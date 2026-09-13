# Modules
import time
from test_cases import *

# Main Function
def merge_sort(arr: list[object]) -> list[object]:

    # Base Case
    if len(arr) < 2:
        return arr
    
    first_half: list[object] = arr[:len(arr) // 2:]
    second_half: list[object] = arr[len(arr) // 2::]

    sorted_first_half: list[object] = merge_sort(first_half)
    sorted_second_half: list[object] = merge_sort(second_half)

    return merge(sorted_first_half, sorted_second_half)

# Helper merge function
def merge(first: list[object], second: list[object]):
    sorted_list: list = []
    i, j = 0, 0
    while len(first) > i and len(second) > j:
        if first[i] < second[j]:
            sorted_list.append(first[i])
            i += 1
        else:
            sorted_list.append(second[j])
            j += 1
    while len(first) > i:
        sorted_list.append(first[i])
        i += 1
    while len(second) > j:
        sorted_list.append(second[j])
        j += 1
    return sorted_list

if __name__ == "__main__":
    first_time = time.time()
    print(merge_sort(integers))
    second_time = time.time()
    print(f"First run took: {round((second_time - first_time), 5)} seconds")
    third_time = time.time()
    print(merge_sort(floats))
    fourth_time = time.time()
    print(f"Second run took: {round((fourth_time - third_time), 5)} seconds")
