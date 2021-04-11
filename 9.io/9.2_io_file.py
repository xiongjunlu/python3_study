############################################ 文件 ############################################

# 打开模式：阅读模式（'r'），写入模式（'w'），追加模式（'a'）
# 文件模式：文本模式（'t'），二进制模式（'b'）
# open默认打开模式：文本模式（text）+ 阅读模式（read）


poem = '''\
Programming is fun
When the work is done 
if you wanna make your work also fun:
    use Python!
'''

# 打开文件以编辑（'w'riting）
f = open('poem.js', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()

# 如果没有特别制定
# 将假定启用默认的阅读（'r'ead）模式
f = open('poem.js')
while True:
    line = f.readline()
    # 零长度只是 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()
