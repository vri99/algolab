from typing import List

"""
Binary search.

Time complexity: O(log n)
Space complexity: O(1)
"""
def binary_search(array: List[int], target: int) -> int | None:
    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        mid: int = (low + high) // 2 # get middle value and round it
        val: int = array[mid]
        if target == val: # if target found return index
            return mid

        if val < target: # cut left side
            low = mid + 1

        if val > target: # cut right side
            high = mid - 1

    return None

