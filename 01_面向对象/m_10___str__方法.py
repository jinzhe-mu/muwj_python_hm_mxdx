"""
在 Python 中，使用 print 输出 对象变量，默认情况下，会输出这个变量 引用的对象 是 由哪一个类创建的对象，以及 在内存中的地址（十六进制表示）
如果在开发中，希望使用 print 输出 对象变量 时，能够打印 自定义的内容，就可以利用 __str__ 这个内置方法了
注意：__str__ 方法必须返回一个字符串
"""


class Cat:
    # 自定义初始化方法
    # 在对象被调用之前第一步调用__init__方法
    def __init__(self, name):
        self.name = name
        print("开始！")

    #
    def __str__(self):
        # 必须返回一个字符串
        return f"我是小猫：{self.name}"

    def __del__(self):
        print("结束！")

    def eat(self):

        print(f"{self.name}在吃小鱼干")


# Tom是一个全局变量，在Tom结束后才回收对象
Tom = Cat("淼淼")
Tom.eat()

# 没有__str__方法时，输出：<__main__.Cat object at 0x00762E68>
# 使用__str__，输出__str__的返回值
print(Tom)


"""
最后输出结果:
开始！
淼淼在吃小鱼干
我是小猫：淼淼
结束！
"""

