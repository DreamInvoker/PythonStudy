# 使用三引号"""可以指定一个多行字符串，如果语句很长，我们可以使用反斜杠(\)来实现多行语句
paragraph = \
    """
        1123
        123123123123123
    """
# print(paragraph)

# 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行
# print(r"\r\n")

# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
# print(u"this is an unicode string")

# 空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# input("\n\n按下 enter 键后退出。")

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：指定末尾字符

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" -- ")
print(y, end=" ")
print()

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

# 调用 python 的 help() 函数可以打印输出一个函数的文档字符串：
# help(max)
# print(max.__doc__)
print(max(1,2))