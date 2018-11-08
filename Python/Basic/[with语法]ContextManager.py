#   上下文管理器(Context Manager)
#   概念: 实现了上下文协议的对象即为上下文管理器
#   上下文协议:  __enter__   __exit__
#   作用: 用于资源的获取和释放
#   当我们使用open()打开一个文件时,要自动进行关闭。此时可以定义上下文管理器进行自动关闭。
#   例如:
#   with open('filename') as file
#       file.read()
#   实现原理:
class File(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

#   with语法使用
with File('a.txt', 'w') as file:
    file.write('ssssss')
