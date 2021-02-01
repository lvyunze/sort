"""
计数排序
"""
import inspect


def sort(_list):
    """
    :param _list: list of values to sort
    :return: sorted values
    """
    try:
        max_value = 0
        for i in range(len(_list)):
            if _list[i] > max_value:
                max_value = _list[i]

        buckets = [0] * (max_value + 1)

        for i in _list:
            buckets[i] += 1
        i = 0

        for j in range(max_value + 1):
            for a in range(buckets[j]):
                _list[i] = j
                i += 1

        return _list

    except TypeError as error:
        print('Counting Sort can only be applied to integers. {}'.format(error))


def time_complexities():
    """
    返回时间复杂度
    :return: string
    """
    return "最好: O(n + k), 平均: O(n + k), 最差: O(n + k)"


def get_code():
    """
    :return: 获取源码
    """
    return inspect.getsource(sort)
