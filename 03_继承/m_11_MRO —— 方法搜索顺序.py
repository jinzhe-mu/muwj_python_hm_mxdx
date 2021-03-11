"""
Python 中针对 类 提供了一个 内置属性 __mro__ 可以查看 方法 搜索顺序
MRO 是 method resolution order，主要用于 在多继承时判断 方法、属性 的调用 路径
print(C.__mro__)
输出结果

(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
在搜索方法时，是按照 __mro__ 的输出结果 从左至右 的顺序查找的
如果在当前类中 找到方法，就直接执行，不再搜索
如果 没有找到，就查找下一个类 中是否有对应的方法，如果找到，就直接执行，不再搜索
如果找到最后一个类，还没有找到方法，程序报错
"""


class A:

    def __init__(self):
        self.num = 10001

    def test(self):
        print("父类A text")

    def demo(self):
        print("父类A demo")

    def deom1(self):
        print("父类A demo1")


class B:

    def __init__(self):
        self.num = 10002

    def demo(self):
        print("父类B demo")

    def test(self):
        print("父类B text")


# 类C继承A类和B类的方法和属性
class C(B, A):
    """多继承可以让子类对象，同时拥有多个父类的方法和属性"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()
print(c.num)
c.deom1()

# 确定C类对象调用父类方法的顺序
print(C.__mro__)
# 查找顺序(按照从左到右的方法查找)：
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# 'object'类是所有类的基类


