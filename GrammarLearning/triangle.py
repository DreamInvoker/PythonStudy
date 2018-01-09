def triangles():
    num = [1]
    while True:
        yield num
        num = [num[i] + num[i - 1] for i in range(1, len(num))]
        num.append(1)
        num.insert(0, 1)


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

res = lambda x: x ** 2

r = map(res, [1, 2, 3, 4])
print(list(r))


def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9}


def str2float(s):
    list = s.split('.')
    intNum = reduce(lambda x, y: x * 10 + y, map(lambda c: DIGITS[c], list[0]))
    floatNum = reduce(lambda x, y: x * 10 + y, map(lambda c: DIGITS[c], list[1]))
    return intNum + floatNum * 10 ** -len(list[1])


def main():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')

if __name__ == '__main__':
    main()
