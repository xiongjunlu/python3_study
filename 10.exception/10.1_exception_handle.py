############################################ 用户输入内容 ############################################

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}', format(text))

# except可以处理指定的错误与异常，或是括号中列出的错误与异常，如果未指定，则处理所有的错误与异常
# try语句执行完成后，在没有发生错误异常时，执行else子句
