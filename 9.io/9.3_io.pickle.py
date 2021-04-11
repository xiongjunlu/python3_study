############################################ Pickle ############################################

# Pickle标准模块，能够将pyhon对象存储在文件中，也能将对象取回

import pickle

# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件
f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()

# 清除 shoplist 变量
del shoplist

# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
print(storedlist)

# 将对象存储到文件中，需要用open方法以写入（'w'）二进制（'b'）的模式打开文件