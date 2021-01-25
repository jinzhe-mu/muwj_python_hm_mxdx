"""
一、在初始化方法内部定义属性
在 __init__ 方法内部使用 self.属性名 = 属性的初始值 就可以 定义属性
定义属性之后，再使用 Cat 类创建的对象，都会拥有该属性
二、改造初始化方法 —— 初始化的同时设置初始值
    在开发中，如果希望在 创建对象的同时，就设置对象的属性，可以对 __init__ 方法进行 改造
把希望设置的属性值，定义成 __init__ 方法的参数
在方法内部使用 self.属性 = 形参 接收外部传递的参数
在创建对象时，使用 类名(属性1, 属性2...) 调用
"""


class Cat:
    # 定义内部私有属性
    def __init__(self, name, color):  # 定义形参
        # print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = name  # 将name形参赋值
        self.color = color

    def eat(self):
        # 调用内部属性
        print(f"{self.color}小猫{self.name}在吃小鱼干！")

    def drink(self):
        # 调用内部属性
        print(f"{self.color}小猫{self.name}在喝热牛奶！")


# 使用类名（）创建爱你对象的时候，会自动调用初始化方法__init__
# 定义对象时给内部属性传入实参
Tom = Cat("巧巧", "奶白")
print(Tom.name)  # 类外部对象调用属性
Tom.eat()

Lazy_cat = Cat("淼淼", "纯黑")
print(Lazy_cat.name)
Lazy_cat.drink()

