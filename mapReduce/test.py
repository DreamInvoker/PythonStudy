# encoding=utf-8
def f(x):
    """实现平方"""
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

# 将列表中的元素转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6])))

from functools import reduce

def add(x,y):
    """两数之和"""
    return x+y


L = [1, 2, 3, 4]
print(reduce(add, L))
print(sum(L))
# sum = reduce(f, L)
print(sum)

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, "  A  B  CD   ")))