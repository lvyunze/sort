"""
插入排序
"""
import inspect


def sort(_list):
    """
    :param _list: list or values to sort
    :return: sort values
    """
    for i in range(1, len(_list)):
        current_number = _list[i]
        for j in range(i - 1, -1, -1):
            if _list[j] > current_number:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
            else:
                _list[j + 1] = current_number
                break
    return _list


def time_complexities():
    """
    时间复杂度
    time complexity
    :return: string
    """
    return "最好: O(n), 平均: O(n ^ 2), 最差: O(n ^ 2)"


def get_code():
    """
    获取源码
    :return: source code
    """
    return inspect.getsource(sort)
