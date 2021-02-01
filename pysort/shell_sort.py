"""
希尔排序
"""
import inspect


def sort(_list):
    """
    :param _list: list of integers to sort
    :return: sorted list
    """
    gap = len(_list) // 2
    while gap > 0:
        for i in range(gap, len(_list)):
            current_item = _list[i]
            j = i
            while j >= gap and _list[j - gap] > current_item:
                _list[j] = _list[j - gap]
                j -= gap
            _list[j] = current_item
        gap //= 2

    return _list


def time_complexities():
    """
    时间复杂度
    time complexity
    :return: string
    """
    return "最好: O(nlogn), 平均: O(depends on gap sequence), 最坏: O(n ^ 2)"


def get_code():
    """
    获取源码
    
    :return: source code
    """
    return inspect.getsource(sort)
