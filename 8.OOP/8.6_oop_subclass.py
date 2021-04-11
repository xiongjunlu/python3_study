############################################ 继承 ############################################

# 增加或修改基类功能，将在所有子类中生效
# 无需在子类中重复父类代码

# coding=UTF-8

class SchoolMember:
    members = 0
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.members += 1
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()

print(SchoolMember.members)

print(SchoolMember.tell(s)) # 子类实例可传入父类方法进行调用，子类实例可看作父类实例


# 注意
# 1.如果子类中定义了__init__方法，父类的__init__方法需要手动显示调用
# 2.如果子类中未定义__init__方法，父类的__init__方法会自动调用
# 3.子类实例调用方法时，首先在子类中寻找方法，若不存在则向基类中寻找方法，以此顺序逐个向上
# 4.元组中有多个基类的情况成为多重继承