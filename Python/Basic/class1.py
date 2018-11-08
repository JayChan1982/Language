class Dog():
    def __init__(self, name, age):
        self.name = name    #属性
        self.age = age

    def print_dog_name(self):
        print("dog's name is " + self.name)


# lucky = Dog("lucky",18)
# lucky.print_dog_name()
# print(lucky.name)
# print(lucky.age)

#   类的继承
#   类名单词首字母大写用大驼峰命名方式
#   继承的时候需要在类名后面括号中标明继承的父类类名 类似: PetDog(Dog)
class PetDog(Dog):
    #   继承时，__init__构造函数，需要通过super()来调用并传递值就入父类
    def __init__(self, name, age):
        super().__init__(name, age)

    #   重写父类函数
    def print_dog_name(self):
        print("the pet dog is not dog's name ")
    #   调用父类方法
    def print_old_dog_name(self):
        super().print_dog_name()

pp = PetDog("allen","20")
print("用重写方法调用子类新方法")
pp.print_dog_name()
print("用super对象调用父类老方法")
pp.print_old_dog_name()

#   类编码风格
#   类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线
#   实例名和模块名都采用小写格式，并在单词之间加上下划线
#   对于每个类，都应紧跟在类定义后面包含一个文档字符串。
#   这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
#   每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
#   可使用空行来组织代码，但不要滥用。
#   在类中，可使用一个空行来分隔方法；
#   而在模块中，可使用两个空行来分隔类。
#   需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import 语句，
#   再添加一个空行，然后编写导入你自己编写的模块的import 语句。
#   在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。



#   属性中用其他类实例作为属性值
#   原因在于当类的属性和方法很多的情况下，需要进一步拆分其他对象进行描述
#   1、保证类的简单性
#   2、保证面向对象的彻底化[万事万物皆对象]
