"""
需求

1、在 Dog 类中封装方法 game
普通狗只是简单的玩耍
2、定义 XiaoTianDog 继承自 Dog，并且重写 game 方法
哮天犬需要在天上玩耍
3、定义 Person 类，并且封装一个 和狗玩 的方法
在方法内部，直接让 狗对象 调用 game 方法
"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name}在蹦蹦跳跳的玩耍")


class XiaoTianDog(Dog):

    def game(self):

        print(f"{self.name}需要在天上玩耍")


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print(f"{self.name}和{dog.name}在玩耍")
        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
wangcai = Dog("旺财")
# wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)

"""
案例小结

Person 类中只需要让 狗对象 调用 game 方法，而不关心具体是 什么狗
game 方法是在 Dog 父类中定义的
在程序执行时，传入不同的 狗对象 实参，就会产生不同的执行效果
多态 更容易编写出出通用的代码，做出通用的编程，以适应需求的不断变化！
"""


