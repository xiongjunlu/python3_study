############################################ global 语句 ############################################

x = 50

def func():
    global x # 在局部作用域指定全局变量：global x, y, z

    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
