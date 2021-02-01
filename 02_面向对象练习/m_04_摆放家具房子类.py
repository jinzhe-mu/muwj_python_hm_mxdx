"""
需求

1、房子(House) 有 户型、总面积 和 家具名称列表
新房子没有任何的家具
    2、家具(HouseItem) 有 名字 和 占地面积，其中
    席梦思(bed) 占地 4 平米
    衣柜(chest) 占地 2 平米
    餐桌(table) 占地 1.5 平米
3、将以上三件 家具 添加 到 房子 中
4、打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

剩余面积

1、在创建房子对象时，定义一个 剩余面积的属性，初始值和总面积相等
2、当调用 add_item 方法，向房间 添加家具 时，让 剩余面积 -= 家具面积
"""


# 创建一个房子类
class House:
    def __init__(self, house_type, area):
        """

        :param house_type:户型
        :param area:面积
        """
        self.house_type = house_type
        self.area = area

        # 剩余面积默认和总面积一致
        self.free_area = area

        # 默认没有任何的家具
        self.item_list = []

    def __str__(self):
        return f"户型:{self.house_type}\n总面积：{self.area}\n"\
            f"剩余面积：{self.free_area}\n摆放的家具有：{self.item_list}"

    def add_item(self, item):
        print(f"要添加家具{item}")

        # 1. 判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            print(f"{item.name}的面积太大，不能添加到房子中")
            return

        # 2. 将家具的名称追加到名称列表中
        self.item_list.append(item.name)
        print(f"目前摆放的家具有：{self.item_list}")
        # 3. 计算剩余面积
        self.free_area -= item.area
        print(f"房子剩余面积是：{self.free_area}")





