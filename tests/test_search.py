from algolab.search import binary_search

def test_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 11) is None

    arr2 = list(range(100000))
    assert binary_search(arr2, 99999) == 99999

    arr3 = [10, 20, 30]
    assert binary_search(arr3, 5) is None