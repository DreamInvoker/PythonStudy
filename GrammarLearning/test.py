import support
import using_name
# from support import print_func
import sys
support.print_func("hello python!")
print(dir(sys))
print(dir(support))
print(dir())

# print("{name},{age}".format({"name":"stephanie","age":"22"}))
print("{name},{age}".format(name=123,age=23))
import math
print("{0:.2f}".format(math.pi))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print("Runoob:{0[Runoob]:d};Google:{0[Google]:d};Taobao:{0[Taobao]:d}".format(table))
print("Runoob:{Runoob:d};Google:{Google:d};Taobao:{Taobao:d}".format(**table))