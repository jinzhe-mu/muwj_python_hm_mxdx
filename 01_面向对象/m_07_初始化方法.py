"""
初始化方法
当使用 类名() 创建对象时，会 自动 执行以下操作：
为对象在内存中 分配空间 —— 创建对象
为对象的属性 设置初始值 —— 初始化方法(init)
这个 初始化方法 就是 __init__ 方法，__init__ 是对象的内置方法
__init__ 方法是 专门 用来定义一个类 具有哪些属性的方法！

在 Cat 中增加 __init__ 方法，验证该方法在创建对象时会被自动调用
"""


class Cat:

    def __init__(self):  # 这是一个初始化方法

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        # 调用内部属性
        print(f"小猫{self.name}在吃小鱼干！")


# 使用类名（）创建爱你对象的时候，会自动调用初始化方法__init__
Tom = Cat()

# 调用类里name的属性
print(Tom.name)
Tom.eat()
