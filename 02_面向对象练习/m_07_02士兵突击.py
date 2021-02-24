"""
士兵突击
需求

士兵 许三多 有一把 AK47
士兵 可以 开火
枪 能够 发射 子弹
枪 装填 装填子弹 —— 增加子弹数量
"""


class Gun:
    def __init__(self):
        # 枪的型号
        self.model = None
        # 枪的初始子弹数
        self.bullet_count = 0

    def add_model(self):
        self.model = input("请给士兵配置枪：")

    def add_bullet(self):
        # 给枪添加子弹计算为int型，输入默认为字符串，要强制转换
        self.bullet_count = int(input("请添加子弹："))

    def shoot(self):

        # 枪，士兵初始没有枪 None 关键字表示什么都没有
        if self.model is None:
            print("士兵没有抢！")
            self.add_model()

        # 判断子弹数量，如果没有子弹返回
        while self.bullet_count <= 0:
            print("你的枪没有子弹")
            # 没有子弹，调用添加子弹方法
            self.add_bullet()

        # 如果有子弹，发射
        while self.bullet_count > 0:
            self.bullet_count -= 1
            print(f"{self.model}发射子弹,剩余{self.bullet_count}颗子弹")
