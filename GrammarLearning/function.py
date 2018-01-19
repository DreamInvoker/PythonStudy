# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(*[1, 2, 3]))
print(calc(*(1, 2, 3)))


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


# 关键字参数

def person(name, age, **kw):
    if 'city' in kw:
        print('city')
    print('name:', name, 'age:', age, 'other:', kw)


person("zengshuang", '22', city='beijing', sex='male')


# 命名关键字参数
def person(name, age, *, city, job):
    """命名关键字参数"""
    pass


person("wuyuting", '22', city='123',job='it')


def product(*x):
    s = 1
    if len(x) == 0:
        raise TypeError
    for a in x:
        s *= a

    return s


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


a = str(input('enter what you want:'))
print('It is',len(a))