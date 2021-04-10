############################################ return 语句 ############################################

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

# 注意：每一个函数都在其末尾隐含了一句 return None，除非显式声明了 return 语句

def some_function():
    print(123)
    pass

print(some_function())

# 注意：pass语句声明一个没有内容的语句块
