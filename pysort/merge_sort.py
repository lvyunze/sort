"""
并归排序
分治法:
分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
"""
import inspect


def merge(a: list, b: list) -> list:
    """
    :param a:左边列表
    :param b:右边列表
    :return:new list
    """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def sort(_list: list) -> list:
    """
    :param _list: 列表
    :return: 并归排序后列表
    """
    if len(_list) in [0, 1]:
        return list(_list)
    else:
        middle = len(_list) // 2
        a = sort(_list[: middle])
        b = sort(_list[middle:])
        return merge(a, b)


def time_complexities():
    """
    :return:并归排序时间复杂度 
    """
    return "最好: O(nlogn), 平均：O(nlogn)， 最差：O(nlogn)"


def get_code():
    """
    :return: 获取源代码
    """
    return inspect.getsource(sort)

