"""
基数排序
"""
import inspect


def sort(_list, base=10):
    """
    :param _list: array to sort
    :param base: base radix number
    :return: sorted list
    """
    # TODO: comment this

    result_list = []
    power = 0
    while _list:
        bs = [[] for _ in range(base)]
        for x in _list:
            bs[x // base ** power % base].append(x)
        _list = []
        for b in bs:
            for x in b:
                if x < base ** (power + 1):
                    result_list.append(x)
                else:
                    _list.append(x)
        power += 1
    return result_list


# 获取源代码
def get_code():
    """
    获取排序源码
    """
    return inspect.getsource(sort)
