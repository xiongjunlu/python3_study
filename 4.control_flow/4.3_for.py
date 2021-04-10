############################################ for 语句 ############################################
rangeList = range(1, 5)
print('range(1, 5)', rangeList)
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

# for循环中else代码块可选，若存在，则它始终会在for循环结束后执行，除非用break语句终止while循环