############################################ 传输元组 ############################################

# 一个函数返回两个不同值，使用元组

def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()

print('errnum ==> ', errnum)
print('errstr ==> ', errstr)

# 注意：a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的元组

# 交换两个值最快方式
a = 5; b = 8
print(a, b)
a, b = b, a
print(a, b)