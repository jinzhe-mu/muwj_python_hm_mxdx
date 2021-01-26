"""
需求

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


xiaoming = Person("小明", 59)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)

del xiaoming

xiaomei = Person("小美", 48)
xiaomei.run()
print(xiaomei)
xiaomei.eat()
print(xiaomei)

del xiaomei


