class Cat:
    """这是一个猫类"""

    def eat(self, color):

        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(f"{color}猫{self.name}爱吃鱼")

    def drink(self, color):

        print(f"{color}小猫{self.name}在喝牛奶")


# 创建第一个猫对象
tom = Cat()

# 设置对象属性：可以用 .属性名  利用复制语句就可以了
tom.name = "Tom "

tom.eat("小白")
tom.drink("黑色")

# 更换属性设置的位置，tom对象中没有name属性，程序报错
# tom.name = "Tom"
"""
程序执行报错如下：
AttributeError: 'Cat' object has no attribute 'name'
属性错误：'Cat' 对象没有 'name' 属性

提示
在日常开发中，不推荐在 类的外部 给对象增加属性
如果在运行时，没有找到属性，程序会报错
对象应该包含有哪些属性，应该 封装在类的内部
"""



