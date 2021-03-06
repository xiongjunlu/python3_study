############################################ 变量 ############################################

# 首字符大小写字母和下划线
# 其余字符大小写字母，数字，下划线 
# 变量只需被赋予某一值。不需要声明或定义数据类型。
# 逻辑行，物理行，\ 显示逻辑行，可将一个逻辑行拆分为多个物理行；

############################################ 数据类型 ############################################

# 数字、字符串、布尔类型、None、对象、类

i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

############################################ 运算符 ############################################

# +（加）
# -（减）
# *（乘）
# **（乘方）
# /（除）
# //（整除）
# %（取模）
# <<（左移）
# >>（右移）
# &（按位与）
# |（按位或）
# ^（按位异或）
# ~（按位取反）
# <（小于）
# >（大于）
# <=（小于等于）
# >=（大于等于）
# ==（等于）
# !=（不等于）
# not（布尔“非”）
# and（布尔“与”）
# or（布尔“或”）
print('1 + 2 ---->', 1 + 2)
print('1 - 2 ---->', 1 - 2)
print('1 * 2 ---->', 1 * 2)
print('1 / 2 ---->', 0 / 2)
print('1 // 2 ---->', 1 // 2)
print('1 % 2 ---->', 1 % 2)
print('1 << 2 ---->', 1 << 2)
print('1 >> 2 ---->', 1 >> 2)
print('1 & 2 ---->', 1 & 2)
print('1 | 2 ---->', 1 | 2)
print('1 ^ 2 ---->', 1 ^ 2)
print('~ 2 ---->', ~ 2)
print('1 < 2 ---->', 1 < 2)
print('1 > 2 ---->', 1 > 2)
print('1 <= 2 ---->', 1 <= 2)
print('1 >= 2 ---->', 1 >= 2)
print('1 == 2 ---->', 1 == 2)
print('1 != 2 ---->', 1 != 2)
print('not True ---->', not True)
print('False and 123 ---->', False and 123)
print('True and 123 ---->', True and 123)
print('True or 123 ---->', True or 123)
print('False or 123 ---->', False or 123)

print('0 or 1', 0 or 1)
print('None or 1', None or 1)
print('0 and 1', 0 and 1)
print('None and 1', None and 1)
print('not None', not None)

############################################ 运算符优先级（最低至最高） ############################################

# lambda：Lambda 表达式
# if - else ：条件表达式
# or：布尔“或”
# and：布尔“与”
# not x：布尔“非”
# in, not in, is, is not, <, <=, >, >=, !=, ==：比较，包括成员资格测试（Membership Tests）和身份测试（Identity Tests）。
# |：按位或
# ^：按位异或
# &：按位与
# <<, >>：移动
# +, -：加与减
# *, /, //, %：乘、除、整除、取余
# +x, -x, ~x：正、负、按位取反
# **：求幂
# x[index], x[index:index], x(arguments...), x.attribute：下标、切片、调用、属性引用
# (expressions...), [expressions...], {key: value...}, {expressions...}：表示绑定或元组、表示列表、表示字典、表示集合

# 具有相同优先级的运算符将从左至右的方式依次进行求值
# 使用括号改变运算顺序