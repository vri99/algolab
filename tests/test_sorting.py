import random

from algolab.sorting import quicksort, selection_sort

def test_quicksort_random() -> None:
    data: list[int] = [random.randint(-1000, 1000) for _ in range(1000)]

    sorted_data: list[int] = quicksort(data)

    assert sorted_data == sorted(data)

def test_selection_sort() -> None:
    data: list[int] = [random.randint(-1000, 1000) for _ in range(1000)]

    sorted_data_test = sorted(data)
    sorted_data: list[int] = selection_sort(data)

    assert sorted_data == sorted_data_test

def test_merge_sort() -> None:
    data: list[int] = [random.randint(-1000, 1000) for _ in range(1000)]

    sorted_data_test = sorted(data)
    sorted_data: list[int] = selection_sort(data)

    assert sorted_data == sorted_data_test