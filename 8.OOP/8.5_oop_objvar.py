############################################ 类变量与对象变量 ############################################

# 类变量（Class Variable）是共享的，可以被属于该类的所有实例访问，类变量改变时，其它所有实例都会得到体现。
# 对象变量（Object variable）不是共享的，每个对象都有属于自己的变量副本，不会与其他对象的变量副本产生关联。

# coding=UTF-8

class Robot:
    """表示有一个带有名字的机器人。"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        # 对象变量
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod # 类方法
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))
    
    @staticmethod # 静态方法
    def how_many2():
        print(123)


# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
# droid1.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here.\n")

# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()

# Robot.how_many()

# print('类文档：', Robot.__doc__)
# print('类方法文档：', Robot.how_many.__doc__)
# print('实例方法文档：', Robot('test').say_hi.__doc__)
# print('实例方法文档：', Robot('test2').die.__doc__)

# Robot.how_many2()
# Robot('123').how_many2()
# Robot.how_many()
# Robot('123').how_many()



# 注意：
# 对象可以通过__class__属性来引用它的类，例如：self.__class__.population
# 类方法装饰器 @classmethod，@staticmethod
# 类文档字符串 Robot.__doc__
# 方法文档字符串 Robot.say_hi.__doc__
# 类方法（@classmethod）的第一个参数是cls，可以用类调用类方法，也可以用实例调用类方法
# 静态方法（@staticmethod）和类的属性与实例无关，但包含该类的逻辑，不适合放在类之外。可以用类调用，也可以用实例调用



class underline:
    def __init__(self, name):
        self.name = name

    def _test():
        print('_test')

    def _test_():
        print('_test_')
    
    def _test__():
        print('_test__')

    def __test(): # 私有属性，类与实例对象均不可访问
        print('__test')
    
    def __test_(): # 私有属性，类与实例对象均不可访问
        print('__test_')

    def __test__():
        print('__test__') 



# underline._test()
# underline._test_()
# underline._test__()
# underline('test')._test()
# underline('test')._test_()
# underline('test')._test__()

# underline.__test()
# underline.__test_()
# underline.__test__()
# underline('test').__test()
# underline('test').__test_()
underline('test').__test__()




# 注意
# 强制约定：类中任何以下双划线开头命名的属性，均为私有变量，外部不可访问。（例如：__privatevar，__privatevar_，不包括：__privatevar__）