############################################ DocStrings ############################################

def print_max(x, y):
    '''打印两个数值中的最大数。
    
    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)

print(print_max.__doc__) # 函数的 __doc__ 属性获取文档字符串
help(print_max) # help()函数也可以获取函数的文档字符串

# 文档字符串位于函数内部作用域第一行（逻辑行）