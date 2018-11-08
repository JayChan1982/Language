"""python操作文件相关的内容"""


# with open("index.html") as html_file :
#     print(html_file.read())

#   文件本身可能有换行符
#   print函数本身也有换行符
#   用rstrip()函数来消除换行符
with open("index.html") as html_file:
    for line in html_file:
        print(line.rstrip())

#   把文件每行都存储入一个列表
with open("index.html") as html_file:
    lines = html_file.readlines()
    print(type(lines))
    print(lines)


# print("文件默认只读模式")
# with open('test.html') as file:
#     lines = file.readlines()
#     print(lines)
#   文件写入模式，会去寻找是否存在
#   如果不存在，会根据文件路径和名称新建
#   如果存在，会清空文件内容，并打开
# print("文件写入模式")
# with open('test.html', 'w') as file2:
#     lines = file2.readlines()
#     print(lines)
print("追加写入模式")
with open('test.html','a') as file3:
    file3.write("<h1>")
    print(lines)

print("读写模式")
with open('test.html','a') as file3:
    lines = file3.readlines()
    print(lines)
    file3.write("<h1>")
    print(lines)