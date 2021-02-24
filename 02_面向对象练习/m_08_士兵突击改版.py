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

        while True:
            # 判断是否开抢
            choice = input("是否开抢：N/Y")
            if choice == "Y":
                # 判断子弹数量，如果没有子弹返回
                while self.bullet_count <= 0:
                    print("你的枪没有子弹")
                    # 没有子弹，调用添加子弹方法
                    self.add_bullet()

                # 如果有子弹，发射
                while self.bullet_count > 0:
                    self.bullet_count -= 1
                    print(f"{self.model}发射子弹,剩余{self.bullet_count}颗子弹")
            else:
                break


class Soldier:

    def __init__(self, name):
        # 姓名
        self.name = name

    def fire(self):

        print(f"士兵{self.name}冲啊！！！")
        ak47.shoot()


ak47 = Gun()
soldier = Soldier("许三多")
soldier.fire()


