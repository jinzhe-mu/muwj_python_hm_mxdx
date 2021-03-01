# 继承的概念：子类 拥有 父类 的所有 方法 和 属性
class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑跑")

    def sleep(self):
        print("睡觉")


#  创建一个方法，继承父类Animal
class Dog(Animal):

    def bark(self):
        print("汪汪叫2")
        # 在子类中使用父类定义的方法
        self.sleep()


class Cat(Animal):

    def catch(self):
        print("小猫喵喵")


class XiaoTianQquan(Dog):

    def fly(self):
        print("它会飞")


# 创建一个对象 --狗对象
# Dog为子类继承了父类Animal，可以使父类的所有方法和属性
xiaohuang = Dog()
xiaohuang.eat()
xiaohuang.run()
xiaohuang.drink()
xiaohuang.sleep()
xiaohuang.bark()
print("--------------------------------------")

# 创建一个对象 --猫对象
# Cat为子类继承了父类Animal，可以使父类的所有方法和属性
miaomiao = Cat()
miaomiao.sleep()
miaomiao.catch()
print("--------------------------------------")

# 创建一个对象 --哮天犬对象
# XiaoTianQuan为子类继承了父类Dog，可以使用父类可使用的所有方法和属性
xtq = XiaoTianQquan()
xtq.drink()
xtq.fly()

"""
结果：
吃
跑跑
喝
睡觉
汪汪叫2
睡觉
--------------------------------------
睡觉
小猫喵喵
--------------------------------------
喝
它会飞

"""
