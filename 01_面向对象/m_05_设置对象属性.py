class Cat:
    """这是一个猫类"""

    def eat(self, color):

        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(f"{color}猫{self.name}爱吃鱼")

    def drink(self, color):

        self.eat(color)
        print(f"{color}小猫在喝牛奶")


# 创建第一个猫对象
tom = Cat()

"""
在 Python 中，要 给对象设置属性，非常的容易，但是不推荐使用
因为：对象属性的封装应该封装在类的内部
只需要在 类的外部的代码 中直接通过 . 设置一个属性即可
注意：这种方式虽然简单，但是不推荐使用！
"""
# 设置对象属性：可以用 .属性名  利用复制语句就可以了
tom.name = "Tom "

print(tom.name)
tom.eat("1.1 小白")
tom.drink("1.2 黑色")


# 创建第二个猫对象
mak = Cat()
mak.name = "Lazy"
mak.eat("2.1 花花")
mak.drink("2.2 灰点")
print(mak)


