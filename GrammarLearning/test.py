# -*- coding:utf-8 -*-


import support
# import using_name
# from support import print_func
import sys

support.print_func("hello python!")
print(dir(sys))
print(dir(support))
print(dir())

# print("{name},{age}".format({"name":"stephanie","age":"22"}))
print("{name},{age}".format(name=123, age=23))
import math

print("{0:.2f}".format(math.pi))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开,
# 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print("Runoob:{0[Runoob]:d};Google:{0[Google]:d};Taobao:{0[Taobao]:d}".format(table))
print("Runoob:{Runoob:d};Google:{Google:d};Taobao:{Taobao:d}".format(**table))
list = ['A','B']
t = ('a','b',list)
list = ['X','Y']
print(t)
str = input("请输入：")
print("您输入的内容是.", str)

# 模式    r   r+  w   w+  a   a+
# 读       *   *         *        *
# 写            *   *    *   *   *
# 创建             *    *    *   *
# 覆盖             *    *
# p开始 *    *  *     *
# p结束                      *    *

# 文件读写默认模式为"r"

# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。
# 在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:</p>
# with open('/tmp/foo.txt', 'r') as f:
#     read_data = f.read()
# f.closed


a = {'Mac Grady': 1, 'YaoMing': 11, 'Wade': 3, 'James': 23, 'Kobe': 24}
name = input('请输入球员的名称，用来查询球衣号码:')
print(name)
sign = a.get(name, False)
if sign == False:
    print('没有该球员，请重新输入\n')
else:
    print(name, '球衣的号码是', sign)
    print('%s 球衣的号码是 %s' % (name, sign))
