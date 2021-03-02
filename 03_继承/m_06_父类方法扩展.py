"""
 对父类方法进行 扩展
如果在开发中，子类的方法实现 中 包含 父类的方法实现
父类原本封装的方法实现 是 子类方法的一部分
就可以使用 扩展 的方式
在子类中 重写 父类的方法
在需要的位置使用 super().父类方法 来调用父类方法的执行
代码其他的位置针对子类的需求，编写 子类特有的代码实现
关于 super
在 Python 中 super 是一个 特殊的类
super() 就是使用 super 类创建出来的对象
最常 使用的场景就是在 重写父类方法时，调用 在父类中封装的方法实现
调用父类方法的另外一种方式（知道）
在 Python 2.x 时，如果需要调用父类的方法，还可以使用以下方式：

父类名.方法(self)
这种方式，目前在 Python 3.x 还支持这种方式
这种方法 不推荐使用，因为一旦 父类发生变化，方法调用位置的 类名 同样需要修改
提示

在开发时，父类名 和 super() 两种方式不要混用
如果使用 当前子类名 调用方法，会形成递归调用，出现死循环
"""


class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑跑")

    def sleep(self):
        print("睡觉")


class Dog(Animal):

    def bark(self):
        print("汪汪叫2")
        # 调用父类的方法
        self.sleep()


class XiaoTianQquan(Dog):

    def fly(self):
        print("它会飞")

    def bark(self):

        # 1、针对子类特有的需求，编写代码.
        print("可以说人类语言")

        # 2、使用 super().父类方法 调用原本在父类中封装的方法
        super().bark()

        # 此方法调动效果同上，但是不建议使用，因为如果要修改父类名，涉及修改点过多
        # 父类名.方法(self)
        # Dog.bark(self)

        # 注意：如果使用子类调用方法，会出现递归调用--死循环！
        # XiaoTianQquan.bark(self)

        # 3、增加子类的其他代码
        print("叫的跟神一样。。。。")


xtq = XiaoTianQquan()

xtq.bark()

