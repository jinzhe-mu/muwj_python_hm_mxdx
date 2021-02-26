"""
提示：在日常开发中，不要使用这种方式，访问对象的 私有属性 或 私有方法

Python 中，并没有 真正意义 的 私有

在给 属性、方法 命名时，实际是对 名称 做了一些特殊处理，使得外界无法访问到
处理方式：在 名称 前面加上 _类名 => _类名__名称
"""


class Wowen2:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print(f"{self.name}的年龄是{self.__age}")


ff2 = Wowen2("rourou")
print(ff2.name)
# print(ff2.__age)
# _类名__名称方式进行访问私有属性，但是不建议
# 伪私有属性，在外界不能被直接访问
print(ff2._Wowen2__age)
# 伪私有方法，同样不允许在外界直接访问
ff2._Wowen2__secret()

"""
结果：
rourou
18
rourou的年龄是18
"""
