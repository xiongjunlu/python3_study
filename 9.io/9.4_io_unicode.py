############################################ Unicode ############################################

# 在读写非英文内容时，需要使用Unicode类型字符串，以字母'u'开头，例如：u"hello world"
# 在网络通信时，需要将Unicode类型字符串转换为 UTF-8 格式，并在这一格式下进行读写操作


# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)

# 注意：在程序中使用Unicode字面量时，必须在程序顶端使用 # encoding=utf-8 这一注释