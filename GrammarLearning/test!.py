# -*- coding: utf-8 -*-
def findMinAndMax(L):
    min = 0
    max = 0
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    if min == 0 and max == 0:
        return (None,None)
    else:
        return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
