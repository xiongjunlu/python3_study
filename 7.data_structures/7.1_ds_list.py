# ############################################ 数据结构 ############################################

# 用来存储一系列相关数据的集合
# 1.列表(List)
# 2.元组(Tuple)
# 3.字典(Dictionary)
# 4.序列(Sequence)
# 5.集合(Set)
# 6.引用(Refer)

############################################ 列表 ############################################
# 列表是可变的数据类型

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ') # 使用 end 参数，通过一个空格结束输出
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
