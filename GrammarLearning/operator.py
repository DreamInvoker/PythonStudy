a = 10
b = 21
a1 = 10.0
b1 = 21.0

c = b / a
print(c)
c = b // a
d = b1 // a1
print(c)
print(d)
c = b % a
print(c)
c = a ** b
print(c)

a = 60
b = 13
print(a & b)
print(a | b)
print(a ^ b)
print(-a - 1)
# & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
# |  按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
# ^ 按位异或运算符：当两对应的二进位相异时，结果为1
# ~ 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
# << 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
# >> 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
print(a << 2)
print(a >> 2)

# Python成员运算符
# 除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
# in 如果在指定的序列中找到值返回 True，否则返回 False。
# not in 如果在指定的序列中没有找到值返回 True，否则返回 False。

# Python身份运算符
# 身份运算符用于比较两个对象的存储单元
# is 是判断两个标识符是不是引用自一个对象 类似 id(x) == id(y)
# is not 是判断两个标识符是不是引用自不同对象 类似 id(a) != id(b)
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a = 4
b = 5
print(b and a)
print(id(a))
print(id(b))
b = 4
print(id(a))
a = 1
b = 1
a += 1
print(a)
print(b)
# 在交互式环境中，编译器会有一个小整数池的概念，会把（-5，256）间的数预先创建好，而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样，比如下例：
a = 100000
b = 100000
print(id(a), id(b))

print(max("12357"))
print(max(1, 2, 3, 4, 2))
print(max(["1", "2"]))

import math

print(math.modf(1.6))
# print(max(range(10)))

# import  random
# print(random.choices(range(10)))
# print(random.shuffle("123456"))

# 文中对于 _ 提到，它代表了上一次的输出结果，"用户应该将其视为只读变量"，实际情况是你也可以对于_ 赋值，_=10 是没有毛病的，但这样的结果会导致你在之后调用 _ 的时候全部变成了10，除非你 del _。
# 对于round:
# >>> round(10.5)
# 10
# >>> round(11.5)
# 12
# >>>
# Python 所谓的奇进偶弃，因为浮点数的表示在计算机中并不准确，用的时候可能要注意一下。
# print(round(10.5));

print(round(11.5))

a = """aaaa"""
a = '''asdasd'''
a = a.capitalize()  # 将字符串的第一个字符转换为大写
a = a.center(15, '*')  # 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print(a.count("t"))  # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

print(a)
print(a.encode())
print(a.encode().decode(encoding= "utf-8",errors="strict"))
a = "\t12"
print(a)
print(a.expandtabs(4))
print(a.find("1"))
# print(a.index("3"))
print(a.isalnum())  # 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
print(a)
print(a.join("*"))
print("".join(a))
print('*'.join(a))
print(a.__len__())
print(len(a))
a = a.lstrip()
# a = max (a)
a="121314"
a = a.replace("1","*",2)  # 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
print(a.rfind("4"))
print(a)
b = a.split("*",1)
print(b)
a = "HelloPython";
print(a.istitle())
a = a.title();
print(a.istitle())
print(a)
a = "1"
a = a.zfill(6)
print(a)