"""
堆排序
"""
import inspect


def sort(_list):
    """
    :param _list: list of values to sort
    :return: sorted values
    """

    # create the heap
    heapify(_list)
    end = len(_list) - 1
    while end > 0:
        _list[end], _list[0] = _list[0], _list[end]
        shift_down(_list, 0, end - 1)
        end -= 1
    return _list


def heapify(_list):
    """
    function helps to maintain the heap property
    :param _list: list of values to sort
    :return: sorted values
    """

    start = len(_list) // 2
    while start >= 0:
        shift_down(_list, start, len(_list) - 1)
        start -= 1


def shift_down(_list, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and _list[child] < _list[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and _list[root] < _list[child]:
            _list[root], _list[child] = _list[child], _list[root]
            root = child
        else:
            return


def time_complexities():
    """
    时间复杂度
    :return: string
    """
    return "最好: O(nlogn), 平均: O(nlogn), 最差: O(nlogn)"


def get_code():
    """
    获取源码
    :return: source code
    """
    return inspect.getsource(sort)
