"""
应用场景

在实际开发中，对象 的 某些属性或方法 可能只希望 在对象的内部被使用，而 不希望在外部被访问到
私有属性 就是 对象 不希望公开的 属性
私有方法 就是 对象 不希望公开的 方法
定义方式

在 定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法
"""


class Wowen:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print(f"{self.name}的年龄是{self.age}")


ff = Wowen("范范")
print(ff.name)
print(ff.age)
ff.secret()
# 方法和属性都没有私有，在函数外可以被正常被调用
"""
结果：
范范
18
范范的年龄是18
"""


class Wowen2:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    # def __secret(self):
    def secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print(f"{self.name}的年龄是{self.__age}")


ff2 = Wowen2("rourou")
print(ff2.name)
ff2.secret()
"""
结果：
rourou
rourou的年龄是18
"""
# 私有属性，在外部是不能够被访问的
# print(ff2.__age)
# 私有方法，同样不允许在外界直接访问
# ff2.__secret()
# 将age属性和secret方法私有后，在函数外不能被调用
# name属性没有私有，可以正常调用
"""
结果：
rourou
Traceback (most recent call last):
  File "E:/PycharmProjects/muwj_python_hm_mxdx/02_面向对象练习/m_12_私有属性和方法.py", line 45, in <module>
    print(ff2.__age)
AttributeError: 'Wowen2' object has no attribute '__age'
"""
