"""
概念

子类 可以拥有 多个父类，并且具有 所有父类 的 属性 和 方法
例如：孩子 会继承自己 父亲 和 母亲 的 特性
"""


class A:

    def test(self):
        print("父类text")


class B:

    def demo(self):
        print("父类demo")


# 类C继承A类和B类的方法和属性
class C(A, B):
    """多继承可以让子类对象，同时拥有多个父类的方法和属性"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()
