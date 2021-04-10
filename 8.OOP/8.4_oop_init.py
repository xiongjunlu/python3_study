############################################ __init__方法 ############################################

# __init__方法会在类的对象实例化时立即运行

class Person3:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person3('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person3('Swaroop').say_hi()