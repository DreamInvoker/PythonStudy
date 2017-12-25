# 面向对象
# 类对象
# 类对象支持两种操作：属性引用和实例化。
#
# 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
#
# 类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# 很多类都倾向于将对象创建为有初始状态的。
# 因此类可能会定义一个名为 __init__() 的特殊方法（构造方法），像下面这样：
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5


# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()


# 类的方法
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()
print(p.age)
print(p.name)


# 继承
class father():
    def __init__(self):
        print('I\'m the father ')


class child(father):
    pass


class child2(father):
    def __init__(self):
        father.__init__()
        print("I\'m child2")

father = father()
child = child()
child2 = child2()

# 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，
# python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
# BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。
# 除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

