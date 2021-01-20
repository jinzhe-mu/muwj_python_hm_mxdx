"""
定义简单的类（只包含方法）
面向对象 是 更大 的 封装，在 一个类中 封装 多个方法，这样 通过这个类创建出来的对象，就可以直接调用这些方法了！
语法格式：
class 类名:

    def 方法1(self, 参数列表):
        pass

    def 方法2(self, 参数列表):
        pass

当一个类定义完成之后，要使用这个类来创建对象，语法格式如下：
对象变量 = 类名()
"""
"""
需求

小猫 爱 吃 鱼，小猫 在 喝 牛奶
分析

定义一个猫类 Cat
定义两个方法 eat 和 drink
按照需求 —— 不需要定义属性
"""


class Cat:
    """这是一个猫类"""

    def eat(self, color):

        print(format(color), "猫爱吃鱼")

    def drink(self, color):

        self.eat(color)
        print(format(color), "小猫再喝牛奶")


# 创建猫对象
tom = Cat()
tom.drink("黑色")
tom.eat("小白")

print(tom)
addr = id(tom)  # 内存地址
print("%d" % addr)  # 按照10进制输出内存地址
print("%x" % addr)  # 按照16进制输出内存地址
