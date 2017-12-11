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
print(a.encode().decode(encoding="utf-8", errors="strict"))
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
a = "121314"
a = a.replace("1", "*", 2)  # 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
print(a.rfind("4"))
print(a)
b = a.split("*", 1)
print(b)
a = "HelloPython";
print(a.istitle())
a = a.title();
print(a.istitle())
print(a)
a = "1"
a = a.zfill(6)
print(a)

a = ()
a = (1)
a = (1,)
print(a)
print(type(a))
a = '''123'''
a = """1234"""
print(end='*')
print(a)


def changeInt(a):
    a = 10
    print(a)


b = 2
print(b)
changeInt(b)
print(b)


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    print(mylist)
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


# changeme()
# 以下是调用函数时可使用的正式参数类型：
#
# 必需参数
# 关键字参数
# 默认参数
# 不定长参数


# 默认参数
# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
print("------------------------")
printinfo("123")


def function():
    "函数_文档描述"
    pass


printinfo(name=1, age=1)


def printinfo(name, *ages):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", ages);
    return;


printinfo("a", 15, 16, 17)

# 匿名函数写法，只包含一条语句
sum = lambda arg1, arg2: arg1 + arg2;
print(sum(10, 20))

# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
#
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
x = int(2.9)  # 内建作用域

g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这这些语句内定义的变量，外部也可以访问，如下代码：
# >>> if True:
# ...  msg = 'I am from Runoob'
# ...
# >>> msg
# 'I am from Runoob'
# >>>

if True:
    msg = "123"
print(msg)

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()

num = 1


def outer():
    num = 10

    def inner():
        # global num   # nonlocal关键字声明
        nonlocal num  # nonlocal关键字声明
        print(num)
        num = 100
        print(num)

    inner()
    print(num)


outer()


# def(**kwargs) 把N个关键字参数转化为字典:
def func(country, province, **kwargs):
    print(country, province, kwargs)


func("China", "Sichuan", city="Chengdu", section="JingJiang")
# func("China","Sichuan",city = "Chengdu", section = "JingJiang")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[:]
print(a)
del a
# print(a)
t = 12345, 54321, 'hello!'
print(t)
print(type(t))
u = t, (1, 2, 3, 4)
print(u)
print(type(u))
# 如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构。
# 在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。

# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
tel = {'irv': 4127, 'guido': 4127, 'jack': 4098}
print(tel.keys())
print(sorted(tel))
print(dict(a=1, b=2))

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for Q, A in zip(questions, answers):
    print("{1}?:{0}".format(Q, A))
# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：

# 元组不可变，若元组的成员可变类型，则成员可编辑。
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
t = a, b, c
print(t)
del b[1:4]
print(t)

# ac = [x*y for x in range[1,5] if x > 2 for y in range[1,4] if x < 3]
# print(ac)

# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块
# （子包），或者包里面定义的其他名称，比如函数，类或者变量。

# import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
#
# 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。