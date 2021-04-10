############################################ 序列 ############################################

# 序列的三种形态：列表、元组与字符串
# 序列的主要功能：
# 1.资格测试（Membership Test），即 in 与 not in 表达式
# 2.索引操作（Indexing Operations），可直接获取序列中的特定项目
# 切片运算符：[:]、[::]，序列切片包括起始位置，不包括结束位置

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# 从某一列表中切片 #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item -3 to 3 is', shoplist[-3:3])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 第一个参数为切片起始位置，第二个参数为切片结束位置，切片不包含结束位置的项，第三个参数为切片步长，默认为1
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1]) # 反向步长-1
