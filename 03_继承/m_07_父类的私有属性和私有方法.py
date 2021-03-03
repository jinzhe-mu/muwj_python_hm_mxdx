class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print(f"私有方法{self.num1}和{self.__num2}")


class B(A):

    def demo(self):

        # 1、访问父类的私有属性 ---在子类的对象方法中，不能访问父类的私有属性
        # 报错：AttributeError: 'B' object has no attribute '_B__num2'
        # print(f"访问父类的私有属性{self.__num2}")

        # 2、调用父类的私有方法 ---在子类的对象方法中，不能访问父类的私有方法
        # 报错：AttributeError: 'B' object has no attribute '_B__text'
        # self.__text
        pass


# 创建一个子类对象
b = B()
print(b)
b.demo()
# 在外界不能直接访问调用对象的私有方法/私有属性
# 报错，不能调用对象的私有属性和私有方法
# print(b.__num2)
# b.__test


