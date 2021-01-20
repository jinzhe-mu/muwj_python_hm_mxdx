class Cat:
    """这是一个猫类"""

    def eat(self, color):

        print(format(color), "猫爱吃鱼")

    def drink(self, color):

        self.eat(color)
        print(format(color), "小猫在喝牛奶")

# tom与mak两个对象调用同一个类，但不是同一个对象


# 创建第一个猫对象
tom = Cat()
tom.eat("1.1 小白")
tom.drink("1.2 黑色")
print(tom)  # 内存地址：0x00A62F58

# 创建第二个猫对象
mak = Cat()
mak.eat("2.1 花花")
mak.drink("2.2 灰点")
print(mak)  # 内存地址：0x00A62FE8

# jek与mak，两个为同一个对象
jek = mak
print(jek)  # 内存地址：0x00A62FE8
