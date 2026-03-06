"""
Quick sort.

Time complexity: O(n log n) -> average case, O(n^2) -> worst case
Space complexity: O(1)
"""
def quicksort(arr: list[int]) -> list[int]:
    if len(arr) < 2: # 1 element left
        return arr

    pivot_index: int = len(arr) // 2
    pivot: int = arr[pivot_index] # get pivot from the middle to gain n log n complexity

    rest = arr[:pivot_index] + arr[pivot_index + 1:] # remove pivot from the sorting process

    less: list[int] = [i for i in rest if i <= pivot]
    greater: list[int] = [i for i in rest if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

"""
Selection sort.

Time complexity: O(n^2)
Space complexity: O(1)
"""
def selection_sort(arr: list[int]) -> list[int]:
    # Go through the whole array
    for i in range(len(arr)):
        smallest_index: int = find_smallest(arr, i) # get smallest's element index in a range

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # swap the smallest element with its current index

    return arr

def find_smallest(arr: list[int], start_from: int) -> int:
    smallest_index: int = start_from # each time start from the previously processed index
    smallest_element: int = arr[smallest_index]

    for i in range(start_from + 1, len(arr)): # range from [... ... ... current index + 1, ...]
        if arr[i] < smallest_element: # if current element is less than the smallest one
           smallest_element = arr[i] # store it
           smallest_index = i

    return smallest_index
