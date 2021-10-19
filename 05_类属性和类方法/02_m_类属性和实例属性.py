"""
* 类属性 就是给 类对象 中定义的 属性
* 通常用来记录 与这个类相关 的特征
* 类属性 不会用于记录 具体对象的特征
"""

"""
示例需求
定义一个 工具类
每件工具都有自己的 name
需求 —— 知道使用这个类，创建了多少个工具对象？
"""

class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象
print("现在创建了 %d 个工具" % Tool.count)
print(f"现在创建了 {Tool.count} 个工具")
