"""
身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用

在 Python 中针对 None 比较时，建议使用 is 判断
运算符	描述	实例
is	is 是判断两个标识符是不是引用同一个对象	x is y，类似 id(x) == id(y)
is not	is not 是判断两个标识符是不是引用不同对象	x is not y，类似 id(a) != id(b)
is 与 == 区别：
is 用于判断 两个变量 引用对象是否为同一个
== 用于判断 引用变量的值 是否相等

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> b is a
False
>>> b == a
True
"""
class Gun:
    def __init__(self):
        # 枪的型号
        # self.model = None
        # 枪的初始子弹数
        self.bullet_count = 0

    # def add_model(self):
    #     self.model = input("请给士兵配置枪：")

    def add_bullet(self):
        # 给枪添加子弹计算为int型，输入默认为字符串，要强制转换
        self.bullet_count = int(input("请添加子弹："))

    def shoot(self):

        # 枪，士兵初始没有枪 None 关键字表示什么都没有
        # if self.model is None:
        #     print("士兵没有抢！")
        #     self.add_model()

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
                    print(f"发射子弹,剩余{self.bullet_count}颗子弹")
            else:
                break


class Soldier:

    def __init__(self, name):
        # 姓名
        self.name = name
        self.gun = None

    def fire(self):

        # 用is 替换==，身份运算符
        # is 用于判断 两个变量 引用对象是否为同一个
        # == 用于判断 引用变量的值 是否相等
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

            return

        print(f"士兵{self.name}冲啊！！！")
        # 在 封装的 方法内部，还可以让 自己的 使用其他类创建的对象属性 调用已经 封装好的方法
        # ak47.shoot() 替换成自己的属性调用其他对象封装好的方法
        self.gun.shoot()


soldier = Soldier("许三多")
# 将对象Gun()给到soldier.gun，让自己定义的属性可以调用另外一个对象封装好的方法
soldier.gun = Gun()
# soldier.gun = ak47
soldier.fire()



