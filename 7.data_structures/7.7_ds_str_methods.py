# ############################################ str类下的对象方法 ############################################

# 这是一个字符串对象
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the String starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != '-1':
    print('Yes, it contains the strint "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
