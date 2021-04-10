############################################ 字符串 ############################################
# 单引号
print('Quote me on this')
# 双引号
print("What's your name?")
# 三引号（多行字符串）
print('''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')


######### format 格式化方法 #########
age = 20
name = 'Swaroop'

# format 格式化字符串，数字代表format方法参数索引
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# format 也可以省略数字
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'  
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# end 指定 print 打印以什么方式结尾
print('a', end='')
print('b', end='')

# 转义序列： \n 换行
print('This is the first line\nThis is the second line')

# 放置在末尾的\ 表示当前字符串将在下一行继续，不会添加新行
print("This is the first sentence. \
This is the second sentence.")

# r或R 指定原始字符串
print(r"Newlines are indicated by \n")

