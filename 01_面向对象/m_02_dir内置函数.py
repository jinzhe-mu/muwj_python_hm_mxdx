"""
在 Python 中 对象几乎是无所不在的，我们之前学习的 变量、数据、函数 都是对象
在 Python 中可以使用以下两个方法验证：

在 标识符 / 数据 后输入一个 .，然后按下 TAB 键，iPython 会提示该对象能够调用的 方法列表
使用内置函数 dir 传入 标识符 / 数据，可以查看对象内的 所有属性及方法
提示 __方法名__ 格式的方法是 Python 提供的 内置方法 / 属性，稍后会给大家介绍一些常用的 内置方法 / 属性

序号	方法名	类型	作用
01	__new__	方法	创建对象时，会被 自动 调用
02	__init__	方法	对象被初始化时，会被 自动 调用
03	__del__	方法	对象被从内存中销毁前，会被 自动 调用
04	__str__	方法	返回对象的描述信息，print 函数输出使用
提示 利用好 dir() 函数，在学习时很多内容就不需要死记硬背了
"""


def demo():
    """这是一个测试函数"""
    print("test")
    good_list = [1, 12]
    print(dir(good_list))
    """
    结果：['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
    '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
    '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
     'sort']
    """


print(dir(demo))
""" 结果：['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__',
 '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__',
 '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__
 kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""
print(demo.__doc__)  # 调用__doc__内置函数输出结果：这是一个测试函数

demo()

