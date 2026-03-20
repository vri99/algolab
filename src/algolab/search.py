"""
Binary search.

Time complexity: O(log n)
Space complexity: O(1)
"""
def binary_search(array: list[int], target: int) -> int | None:
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

"""
Prefix Sum.

Time complexity: O(n)
"""
def prefix_sum(array: list[int], target: int) -> int | None:
    prefix_sum_set: dict[int, int] = {0: 1}
    current_sum: int = 0
    total_target: int = 0

    for i in range(len(array)):
        # accumulate all sum with current int
        current_sum += array[i]
        # add all known sums starting from index: 0
        prefix_sum_set[current_sum] = prefix_sum_set.get(current_sum, 0) + 1

        # increment each found range of sum of elements that = target
        if prefix_sum_set.get(current_sum - target) is not None:
            total_target += prefix_sum_set[current_sum - target]

    # return total number of found ranges
    return total_target