class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑跑")

    def sleep(self):
        print("睡觉")


class Dog:

    def eat(self):
        print("吃2")

    def drink(self):
        print("喝2")

    def run(self):
        print("跑跑2")

    def sleep(self):
        print("睡觉2")

    def bark(self):
        print("汪汪叫2")


# 创建一个对象 --狗对象
xiaohuang = Animal()
xiaohuang.eat()
xiaohuang.run()
xiaohuang.drink()
xiaohuang.sleep()
# 创建一个对象 --另一个狗对象
xiaohuangx = Dog()
xiaohuangx.eat()
xiaohuangx.run()
xiaohuangx.drink()
xiaohuangx.sleep()
xiaohuangx.bark()


