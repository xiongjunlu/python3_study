############################################ 标准库模块 ############################################
# 1.创建模块方式1：创建包含函数和变量的.py文件
# 2.创建模块方式2：使用python解释器语言编写模块（CPython, JPython, IronPython, PyPython）

import sys
import os

print(os.getcwd()) # 查看目前程序所在目录

print('The command line arguments are:')
for i in sys.argv: # sys.argv 终端输入的命令行参数列表
    print(i)

for i in sys.path:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 注意：
# 1.如果导入未编译的模块，那么python解释器将从sys.path提供的目录中进行查找，因此必须将模块放置在sys.path所列出的目录中
# 2.sys.path的第一个元素是当前文件所在目录
# 3.运行的脚本名称会在sys.argv列表中第一位

############################################ 按字节码编译的 .pyc 文件 ############################################

# 1..py转换为中间形式的文件.pyc
# 2.导入.pyc文件更加快速，因为导入模块的部分操作.pyc文件已经完成
# 3..pyc文件独立于平台运行
# 4.通常.pyc文件与.py文件在同一目录，如果对某一目录没有写入文件的权限，则无法生成.pyc文件
# 5.当模块第一次被导入时将被执行，

############################################ from..import 语句 ############################################

from math import sqrt
print("Square root of 16 is", sqrt(16))

# 注意：为了避免名称冲突，应该尽量使用import语句，而不是 from...import 语句
