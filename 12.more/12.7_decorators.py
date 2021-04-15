############################################ 装饰器 ############################################

# 装饰器用于包装修改其他函数功能的函数

from time import sleep
from functools import wraps 
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f) # @wraps接收一个函数进行装饰，确保被装饰器包装后，函数名字（__name__）与注释文档（docstring）依然为原来函数本身声明的
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                print(0+attempt)
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s%s failed : %s", attempt, MAX_ATTEMPTS, (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attemtps failed : %s", MAX_ATTEMPTS, (args, kwargs))
    return wrapped_f

counter = 0

@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    # 这将在第一次调用时抛出异常
    # 在第二次运行时将正常工作（也就是重试）
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database("Some bad value")



# ############################################ 装饰器使用场景 ############################################

# # 1.授权（Authorization）
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated


# # 2.日志（Logging）
# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging
 
# @logit
# def addition_func(x):
#    """Do some math."""
#    return x + x
 
# result = addition_func(4)


############################################ 带参数的装饰器 ############################################
# # 1.返回包裹函数的装饰器函数
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile，并写入内容
#             with open(logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的logfile
#                 opened_file.write(log_string + '\n')
#             return func(*args, **kwargs)
#         return wrapped_function
#     return logging_decorator
 
# @logit()
# def myfunc1():
#     pass
 
# myfunc1()
# # Output: myfunc1 was called
# # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
 
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
 
# myfunc2()
# # Output: myfunc2 was called
# # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串


############################################ 装饰器类 ############################################
# 用类构建装饰器

# class logit(object):
#     def __init__(self, logfile='out.log'):
#         self.logfile = logfile
 
#     def __call__(self, func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile并写入
#             with open(self.logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的文件
#                 opened_file.write(log_string + '\n')
#             # 现在，发送一个通知
#             self.notify()
#             return func(*args, **kwargs)
#         return wrapped_function
 
#     def notify(self):
#         # logit只打日志，不做别的
#         pass

# @logit()
# def myfunc1():
#     pass

# class email_logit(logit):
#     '''
#     一个logit的实现版本，可以在函数调用时发送email给管理员
#     '''
#     def __init__(self, email='admin@myproject.com', *args, **kwargs):
#         self.email = email
#         super(email_logit, self).__init__(*args, **kwargs)
 
#     def notify(self):
#         # 发送一封email到self.email
#         # 这里就不做实现了
#         pass