############################################ self ############################################

# 类方法的第一个参数必须是self字段，self引用对象本身

class MyClass:
    def method(self):
        print(self)

obj = MyClass()
obj.method()

# myobject.method(arg1, arg2) Python将其转换为 MyClass.method(myobject, arg1, arg2)