"""
提示：
在 对象的方法内部，是可以 直接访问对象的属性 的
同一个类 创建的 多个对象 之间，属性 互不干扰！

需求：
小明 和 小美 都爱跑步
小明 体重 75.0 公斤
小美 体重 45.0 公斤
每次 跑步 都会减少 0.5 公斤
每次 吃东西 都会增加 1 公斤
"""


class Person:
    """人类"""
    # 定义内部属性姓名和体重
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    # 返回名字和体重，输出对象
    def __str__(self):
        return f"我的名字叫{self.name}，我的体重是{self.weight}公斤"

    # 当锻炼身体时调用run，体重减0.5
    def run(self):
        print(f"{self.name}爱跑步,跑步锻炼身体")
        self.weight -= 0.5

    # 当吃东西的时候调用eat，体重增加1
    def eat(self):
        print(f"{self.name}爱吃零食，容易变胖")
        self.weight += 1


xiaoming = Person("小明", 75)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)


xiaomei = Person("小美", 45)
xiaomei.run()
print(xiaomei)
xiaomei.eat()
print(xiaomei)
print(xiaoming)  # xiaomei的调用不会影响xiaoming的调用结果


"""
结果：
小明爱跑步,跑步锻炼身体
我的名字叫小明，我的体重是74.5公斤
小明爱吃零食，容易变胖
我的名字叫小明，我的体重是75.5公斤
小美爱跑步,跑步锻炼身体
我的名字叫小美，我的体重是44.5公斤
小美爱吃零食，容易变胖
我的名字叫小美，我的体重是45.5公斤
我的名字叫小明，我的体重是75.5公斤
"""

