############################################ logging模块 ############################################

# 通过logging模块将程序运行时的日志信息存储在某个地方

import os # 操作系统交互模块
import platform # 平台（操作系统）信息模块
import logging # 日志模块

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(
        os.getenv('HOMEDRIVE'), 
        os.getenv('HOMEPATH'), 
        'test.log'
    )
else:
    logging_file = os.path.join( # os.path.join函数确保完整的位置路径符合当前操作系统预期格式
        os.path.dirname(os.path.abspath(__file__)), # 获取当前文件所在目录的绝对路径
        'test.log'
    )
print("Logging to", logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

print(platform.platform())
print(os.getenv('HOME'))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.getenv('HOME'), __file__))