############################################ 抛出异常 ############################################

# 通过raise语句抛出错误或异常，以及异常对象。
# 抛出的错误或异常必须是Exception类的派生类。

# encoding=UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
        '{0} long, expected at least {1}')
        .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

# 注意：通过as操作符，将异常类的实例对象，存储为相应的错误名或异常名
