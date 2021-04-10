############################################ 模块的 __name__ ############################################

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

print('__name__:', __name__)

# 注意：
# 1.模块的 __name__ 属性值表示当前模块运行时所处的模块名称（独立运行 or 导入运行）
# 2.如果模块独立运行，则模块的 __name__ 属性值为 '__main__'
# 3.如果模块被导入到其他模块运行，则模块的 __name__ 属性值为导入模块的名称