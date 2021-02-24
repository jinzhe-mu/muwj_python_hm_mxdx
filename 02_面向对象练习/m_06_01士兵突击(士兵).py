import m_07_02士兵突击

"""
士兵突击
需求

士兵 许三多 有一把 AK47
士兵 可以 开火
枪 能够 发射 子弹
枪 装填 装填子弹 —— 增加子弹数量
"""


class Soldier:

    def __init__(self, name):
        # 姓名
        self.name = name

    def fire(self):
        # 判断是否有枪
        # 如果有枪
        print(f"士兵{self.name}冲啊！！！")
        ak47.shoot()


ak47 = m_07_02士兵突击.Gun()
soldier = Soldier("许三多")
soldier.fire()



