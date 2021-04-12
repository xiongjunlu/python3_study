############################################ Try...Finally ############################################

import sys
import time

f = None
try:
    f = open("./poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush() # python输出有可能被缓冲，该语句将缓冲区内容立即输出至屏幕，并清空缓冲区
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt: # ctrl+c 中断程序运行
    print("!! You cancelled the reading from the file.")
finally: #程序退出前，finally子句将被执行
    if f:
        f.close()
    print("(Cleaning up: Close the file)")