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


# 创建一个家具类
class HouseItem:
    def __init__(self, name, area):
        """

        :param name: 家具名称
        :param area: 占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name}占地面积是{self.area}"




