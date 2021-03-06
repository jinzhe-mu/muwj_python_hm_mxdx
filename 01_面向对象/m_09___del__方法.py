"""
在 Python 中：
当使用 类名() 创建对象时，为对象 分配完空间后，自动 调用 __init__ 方法
当一个 对象被从内存中销毁 前，会 自动 调用 __del__ 方法

应用场景：
__init__ 改造初始化方法，可以让创建对象更加灵活
__del__ 如果希望在对象被销毁前，再做一些事情，可以考虑一下 __del__ 方法

生命周期：
一个对象从调用 类名() 创建，生命周期开始
一个对象的 __del__ 方法一旦被调用，生命周期结束
在对象的生命周期内，可以访问对象属性，或者让对象调用方法
"""


class Cat:
    # 自定义初始化方法
    # 在对象被调用之前第一步调用__init__方法
    def __init__(self, name):
        self.name = name
        print("开始！")

    # 在对象被调用销毁前，最后调用__del__方法
    def __del__(self):
        print("结束！")

    def eat(self):

        print(f"{self.name}在吃小鱼干")


# Tom是一个全局变量，在Tom结束后才回收对象
Tom = Cat("淼淼")
Tom.eat()

print("-" * 50)  # __del__方法在输出-之后执行

# 在执行del方法之前，会先去调用__del__方法
del Tom  # 将对象回收（del 关键字可以删除一个对象）

print("*" * 50)  # __del__方法在输出*之前执行

"""
最后输出结果
开始！
淼淼在吃小鱼干
--------------------------------------------------
结束！
**************************************************
"""

