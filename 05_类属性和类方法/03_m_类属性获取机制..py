"""
在 Python 中 属性的获取 存在一个 向上查找机制
因此，要访问类属性有两种方式：
类名.类属性
对象.类属性 （不推荐）
注意
如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会影响到 类属性的值
"""

class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1



tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 类名.类属性
print(f"现在创建了 {Tool.count} 个工具aaa")

# python有向上查找机制，从下往上查找到第一个count，就会直接使用，如果查找不到，再继续向上查找
# 对象.类属性 （不推荐）
print(f"现在创建了 {tool1.count} 个工具bbb")
