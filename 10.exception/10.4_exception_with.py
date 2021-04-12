############################################ with 语句 ############################################

# 避免重复显示使用 try...finally 语句，用with语句代替

with open('poem.txt') as f:
    for line in f:
        print(line, end='')

# with语句使用的协议（Protocol），将获取open方法返回的“thefile”对象
# 在代码块执行前访问thefile.__enter__函数，执行后访问thefile.__exit__函数