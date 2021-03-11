"""
问题的提出

如果 不同的父类 中存在 同名的方法，子类对象 在调用方法时，会调用 哪一个父类中的方法呢？
提示：开发时，应该尽量避免这种容易产生混淆的情况！ —— 如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承
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
"""
结果：
父类B text
父类B demo
10002
父类A demo1
"""

