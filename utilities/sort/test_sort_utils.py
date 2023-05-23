from sort_utils import *

__UNSORTED_LIST = [5, 2, 9, 1, 7]
__SORTED_LIST = [1, 2, 5, 7, 9]

def test_bubble_sort():
    assert bubble_sort(__UNSORTED_LIST) == __SORTED_LIST

def test_quick_sort():
    assert quick_sort(__UNSORTED_LIST) == __SORTED_LIST