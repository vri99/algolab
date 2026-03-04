# def binary_search(array, value):
#     low = 0
#     high = len(array) - 1
#     count = 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = array[mid]
#
#         if guess == value:
#             return mid, count
#
#         count += 1
#
#         if guess < value:
#             low = mid + 1
#
#         if guess > value:
#             high = mid - 1
#
#     return -1
#
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ], 2))

# def find_smallest(array):
#     smallest_value = array[0]
#     smallest_index = 0
#
#     for i in range(1, len(array)):
#         if smallest_value > array[i]:
#             smallest_value = array[i]
#             smallest_index = i
#
#     return smallest_index
#
# def selection_sort(arr):
#     result_array = []
#
#     for i in range(len(arr)):
#         smallest_index = find_smallest(arr)
#
#         result_array.append(arr.pop(smallest_index))
#
#     return result_array
#
# print(selection_sort([4, 6, 2, 1, 10, 232, 22, 11, 3, 9]))

# def sum_(arr):
#     if not arr:
#         return 0
#     else :
#         return 1 + sum_(arr[1:])
# #
# print(sum_([1,2,3, 5, 10]))

# def qs(arr):
#     if len(arr) < 2:
#         return arr
#
#     pivot = arr[0]
#     less = [i for i in arr[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]
#
#     return qs(less) + [pivot] + qs(greater)
#
# print(qs([1,4,6,8,9,3,2]))

