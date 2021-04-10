############################################ 可变参数 ############################################

def total(a=5, *numbers, **phonebook):
    print('a', a)
    print('numbers==>', numbers)
    print('phonebook==>', phonebook)

    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

# 注意：
# 1.函数参数数量可变
# 2.*numbers 星号参数，此处开始到结束的所有位置参数都汇集为一个 numbers 元组
# 3.**phonebook 双星号参数，此处开始到结束的所有关键字参数都汇集为一个 phonebook 字典