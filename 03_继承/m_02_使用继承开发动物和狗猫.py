"""
子类 继承自 父类，可以直接 享受 父类中已经封装好的方法，不需要再次开发
子类 中应该根据 职责，封装 子类特有的 属性和方法
"""


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


"""
1) 继承的语法
class 类名(父类名):
    pass
    
子类 继承自 父类，可以直接 享受 父类中已经封装好的方法，不需要再次开发
子类 中应该根据 职责，封装 子类特有的 属性和方法

2) 专业术语
Dog 类是 Animal 类的子类，Animal 类是 Dog 类的父类，Dog 类从 Animal 类继承
Dog 类是 Animal 类的派生类，Animal 类是 Dog 类的基类，Dog 类从 Animal 类派生

3) 继承的传递性
C 类从 B 类继承，B 类又从 A 类继承
那么 C 类就具有 B 类和 A 类的所有属性和方法
子类 拥有 父类 以及 父类的父类 中封装的所有 属性 和 方法

提问:
哮天犬 能够调用 Cat 类中定义的 catch 方法吗？

答案:
不能，因为 哮天犬 和 Cat 之间没有 继承 关系
"""

