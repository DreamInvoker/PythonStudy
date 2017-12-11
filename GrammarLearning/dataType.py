# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值


# Python允许你同时为多个变量赋值
a = b = c = 1  # 三个变量被分配到相同的内存空间上
# Python3 支持 int、float、bool、complex（复数）。没有 python2 中的 Long。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
# print(type(a), type(b), type(c), type(d))
print(isinstance(a, float))


# isinstance 和 type 的区别在于：
class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False

# 区别就是:
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。


#  2 // 4 # 除法，得到一个整数
# 17 % 3 # 取余
#  2 ** 5 # 乘方
# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
# 4、在混合计算时，Python会把整型转换成为浮点数。


str = 'Runoob'

print(str)  # 输出字符串     Runoob
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符    Runoo
print(str[0])  # 输出字符串第一个字符 R
print(str[2:5])  # 输出从第三个开始到第五个的字符  noo
print(str[2:])  # 输出从第三个开始的后的所有字符   noob
print(str * 2)  # 输出字符串两次       RunoobRunoob
print(str + "TEST")  # 连接字符串    RunoobTEST

# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。



# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号([])之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 与Python字符串不一样的是，列表中的元素是可以改变的


# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号


# string、list和tuple都属于sequence（序列）。

# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。

# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建空集合
a = set()
a = {1, 2, 3, 4, 4, 5, 5, 5, 5}
print(a)
if 7 not in a:
    print("7不在a里面")
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(b)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型。

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：

dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}
{x: x ** 2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
b = dict(Runoob=1, Google=2, Taobao=3)
print(b)
{'Taobao': 3, 'Runoob': 1, 'Google': 2}

# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
b.clear()
print(b)

# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }
x = 1
# int(x [,base])
# 将x转换为一个整数
float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
chr(x)
# 将一个整数转换为一个字符
# unichr(x)
# 将一个整数转换为Unicode字符
# ord(x)
# 将一个字符转换为它的整数值
hex(x)
# 将一个整数转换为一个十六进制字符串
oct(x)


# 将一个整数转换为一个八进制字符串


# python中的函数还可以接收可变长参数，比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上。
def test(*args):
    print(args)
    return args


print(type(test(1, 2, 3, 4)))
print(test(1, 2, 3))
# 在list的使用中，开始时很容易忽视的一点是：
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list[1:3])  # 从第二个开始输出到第三个元素
print (list[2])
print (list[2:3])
# 这两句话打印的内容其实是一样的，但是第二句话有中括号


# type 是用于求一个未知数据类型对象，而 isinstance 是用于判断一个对象是否是已知类型。
# type 不认为子类是父类的一种类型，而isinstance会认为子类是父类的一种类型。
# 可以用 isinstance 判断子类对象是否继承于父类，type 不行。
# 综合以上几点，type 与 isinstance 虽然都与数据类型相关，但两者其实用法不同，type 主要用于判断未知数据类型，isinstance 主要用于判断 A 类是否继承于 B 类：
# 判断子类对象是否继承于父类
class father(object):
    pass
class son(father):
    pass
if __name__ == '__main__':
    print(type(son())==father)
    print (isinstance(son(),father))
    print (type(son()))
    print (type(son))

# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
