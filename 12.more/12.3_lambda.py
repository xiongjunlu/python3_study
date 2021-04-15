############################################ Lambda语句 ############################################

# lambda类似匿名函数，减少代码冗余，可读性更强
# lambda匿名函数也可直接复制给变量，之后想正常函数一样调用：c = lambda x,y,z: x*y*z
# 可在lmbda函数后直接传递参数：(lambda x:x**2)(3)
# lambda语法：lambda argument_list:expersion
#   - argument_list：参数列表
#   - expersion：单行表达式
# 表达式的值作为lambda函数的返回值


points = [
    {'x': 2, 'y': 3},
    {'x': 4, 'y': 1}
]

points.sort(key = lambda i: i['y'])
print(points)

filt = filter(lambda x: x%3 == 0, [1,2,3,4,5,6])
print(list(filt))

squares = map(lambda x: x**2, range(5))
print(list(squares))



# 元组列表排序，sorted结合
a = [('b',3),('a',2),('d',4),('c',1)]
sort1 = list(sorted(a, key = lambda x: x[0])) # 按照第一个元素排序
print(sort1)
sort2 = list(sorted(a, key = lambda x: x[1])) # 按照第二个元素排序
print(sort2)



# reduce结合使用
from functools import reduce
print(reduce(lambda a,b: '{},{}'.format(a,b), [1,2,3,4,5,6,7,8,9]))



# 嵌套使用，lambda函数作为return值
def increment(n):
    return lambda x: x+n
f = increment(4)
print(f(2))



# 字符串拼接
x = (lambda x='Boo',y='Too',z='Z00': x + y + z)
print(x('Foo'))



# 在tkinter中定义内联的callback函数
import sys
from tkinter import Button,mainloop
x = Button(text='Press me', command=(lambda : sys.stdout.write('Hello,World\n')))
x.pack()
# x.mainloop()



# 判断字符串是否以某个字母开头
Names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
B_Name= filter(lambda x: x.startswith('B'), Names)
print(list(B_Name))



# 求两个列表元素之和
b = [1,2,3,4]
c = [5,6,7,8]
print(list(map(lambda x, y: x+y, b, c)))



# 字符串每个单词长度
sentence = "Welcome To Beijing!"
words = sentence.split()
lengths = map(lambda x: len(x), words)
print(list(lengths))



# # 列表解析：遍历iterable，然后逐个执行expression，根据执行结果生成列表
# #     [expression for iter_val in iterable]
# #     [expression for iter_val in iterable if cond_expr]

# def sq(x):
#     return x*x

# print(map(sq,[y for y in range(10)]))

# print([y*2 for y in range(10) if (y % 2 == 0)])

