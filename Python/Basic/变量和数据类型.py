#   Python之禅
#   一些Python开发的重要建议
import this

#   代码编写要易于阅读，因为写代码的时间没有读代码的时间长，
#   并且团队合作必须要让别人快速的能够读懂你的代码
#   PEP8 原则
#   1、每级缩进都用4个空格
#   2、在开发中不要混用制表符和空格
#   3、IDE工具一般都提供设置制表符所代表的空格的数量
#   4、每行文本字符不超过72个(有些编译器会加一些格式)，不超过72个字符可以一个屏幕看两个程序,编译器一般会用竖线来提醒
#   5、在诸如 ==、>=、<=、等比较运算两边各添加一个空格
#   6、一个函数只做一件事情，要把事件动作细颗粒化
#   7、

#   变量
#   字符串 str
message_str = " this is a dog "
message2_str = " , that's good!"
print(type(message_str))

#   数字 int
calc_int = 18
print(type(calc_int))

#   加法
print( 3 + 5)

#   减法
print(10 - 2)

#   乘法
print(2 * 4)

#   除法
print(16 / 2)

#   浮点 float
calc_int2   = 18.26
print(type(calc_int2))

#   求模运算=求余数
print( 4 % 3)
print( 6 % 3)

#   列表 list
#   是有序的集合，可以通过索引值直接访问，索引从0开始
#   列表元素是可以修改的，区别于元组
#   程序处理期间用来承载可变化的数据集合的需求
colors = ['red', 'black', 'pink', 'green', 'blue']

#   列表为空时，返回false, 不为空时返回 True
empty_list = []
if(empty_list):
    print("True")
else:
    print("false")


#   列表访问方式1
print(colors[0])

#   修改列表元素
colors[0] = 'deepred'
print(colors)

#   添加列表元素[末尾追加]
colors.append('grown')
print(colors)

#   添加列表元素[任意位置]
#   第一个参数: 索引值
#   第二个参数: 值
colors.insert(0, 'yellow')
print(colors)

#   删除列表元素[尾部删除]
#   函数返回弹出元素
#   注意: 列表元素删除后，还需要使用这个删除元素，推荐使用pop函数
colors.pop()
print(colors)

#   删除列表元素[任意位置]
#   函数返回弹出元素
#   注意: 列表元素删除后，还需要使用这个删除元素，推荐使用pop函数
colors.pop(0)
print(colors)

#   删除列表元素[任意位置]
#   del语句直接删除，没有任何返回
#   注意: 纯列表元素删除，推荐使用del语句
del colors[0]
print(colors)

#   删除列表元素[通过元素值]
#   函数返回删除元素
#   注意: remove函数只删除列表中第一个完全匹配值的元素，其他匹配值不做任何处理
#   需要通过循环去处理列表中多次出现的相同值的元素
colors.remove('blue')
print(colors)

#   列表的组织
#   排序[永久性]
#   默认按字母顺序排列[升序]
#   大写和小写对于列表排序是有影响的，如果要消除这个影响，需要先把列表元素都处理成大写或小写，再进行排序
colors.sort()
print(colors)

#   排序[永久性]
#   参数: reverse = true 按字母顺序排序[降序]
#   大写和小写对于列表排序是有影响的，如果要消除这个影响，需要先把列表元素都处理成大写或小写，再进行排序
colors.sort(reverse=True)
print(colors)

#   排序[临时性]
#   默认按字母顺序排列[升序]
#   大写和小写对于列表排序是有影响的，如果要消除这个影响，需要先把列表元素都处理成大写或小写，再进行排序
print(sorted(colors))

#   排序[临时性]
#   参数: reverse = true 按字母顺序排序[降序]
#   大写和小写对于列表排序是有影响的，如果要消除这个影响，需要先把列表元素都处理成大写或小写，再进行排序
print(sorted(colors, reverse=True))

#   列表元素反转[永久性]
#   注意: 非排序，而是将原列表元素按照前到后的次序，反转成后到前排列
colors.reverse()
print(colors)

#   列表的长度
print(len(colors))

#   列表的遍历
for color in colors:
    print(color + '==>')

#   数字列表
#   生成数字列表
#   第一个参数:  开始数字[包含]
#   第二个参数:  结束数字[不包含]
#   第三个参数:  步长值[默认不输入任何参数的情况下是1]
#   注意: list()是生成一个空白的列表
nums = list(range(1,10,2))
print(nums)

#   数字列表遍历
for num in  range(1,10):
    print(str(num) + "==>")

#   数字列表简单的统计计算
#   求和
print(sum(nums))

#   最小值
print(min(nums))

#   最大值
print(max(nums))

#   列表解析
#   目的: 减少代码输入，高效易读
#   定义一个nums列表，里面的值是value ** 2, 而value值的来源是通过for循环进行的
nums = [value ** 2 for value in  range(1,11,2)]
print(nums)

#   列表解析测试代码
#   目的: 3-30之内，能被3整除的数字的平方
#   定义一个nums列表，里面的值是value ** 2,而value得值来源是通过for循环进行得，并且通过if条件过滤掉不能被3整除得数字
nums = [value ** 2 for value in range(3,31) if(value % 3 == 0)]
print(nums)

#   列表切片[临时性]
#   不会对原列表产生任何修改
#   索引值可以为负数 索引的排列为 左面开始数是从0开始， 右面开始数是从-1开始，
#   注意: 索引值必须都从左往右输入,类似: 0:3  -3:-1
#   第一个参数: 切片开始的索引值[如第一个参数省略不写，默认从0开始]
#   第二个参数: 切片结束的索引值[如第二个参数省略不写，默认到列表结尾]
#   第三个参数: 切片的步长值
#   案例代码1
print(nums[0:3])
#   案例代码2
#   省略第一个参数，从索引值0:3
print(nums[:3])
#   案例代码3
#   省略第一个参数，从索引值0:3步长为2
print(nums[:3:2])
#   案例代码4
#   省略第二个参数，从索引值0:末尾步长为2
print(nums[0::2])
#   案例代码5
#   从索引值-3:-1步长为2
#   索引为负数时，必须从左往右给参数
print(nums[-3:-1:2])
#   案例代码6
#   索引值为-3:末尾步长为2
print(nums[-3::2])

#   切片遍历
for num in nums[:]:
    print(str(num) + "="*2+">")

#   列表复制
#   直接列表变量赋值[不生成新列表，与原来列表共享同一个内存]
#   两个ID相同，指向同一个列表
nums_new = nums
print(id(nums_new))
print(id(nums))
#   通过切片赋值[生成新列表，是原来列表的副本]
#   两个ID不相同，指向不同的列表
nums_new = nums[:]
print(id(nums_new))
print(id(nums))

#   元组
#   元组是不可变的列表
#   程序处理期间，用来承载不可变的元素集合的需求
#   在整个程序生命周期内，不变的值的集合，都可以通过元组来进行承载
#   除了与列表元素修改相关的操作不具备外，其他操作根列表相同
#   定义个空的tuple  nums_tuple = ()
nums_tuple = (200,188)

#   访问元组元素
print(nums_tuple[0])

#   遍历元组[操作方式同列表]
for num in nums_tuple:
    print(str(num)+'='*2+'>')
#   案例代码
#   需求: 餐厅原来有5中简单的餐食
#   1、meat  2、tea  3、milk  4、bread  5、hot
#   由于市场不景气，客户口味变化，把meat和hot给取消了，然后新增了 flower和coffee两个餐食
kitchen_foods = ('meat', 'tea', 'milk', 'bread', 'hot')
print(kitchen_foods)
kitchen_foods = sorted(kitchen_foods[1:4] + ('flower', 'coffee'))
print(kitchen_foods)

#   字典 dict
#   字典第一个是KEY值
#   字典第二个是VALUE值
#   字典是无序的，因为字典关心键和值的关联，不关心字典内元素的位置
#   字典遍历时，存储的次序与返回的次序可能不一致
#   定义一个空字典 alien = {}
#   定义一个颜色和点数的字典
alien = {"color":"red","point":5}

#   访问字典元素
print(type(alien))
print(alien["color"])

#   添加字典元素
alien["position_x"] = 0
alien["position_y"] = 25
print(alien)

#   删除字典元素[永久性]
del alien["position_x"]
print(alien)

#   定义多键-值对
alien = {
    "color":"red",
    "point":5,
    "position_x":0,
    "position_y":0
}
print(alien)

#   遍历字典
#   遍历字典时，存储的次序与返回的次序可能不一致
#   遍历字典时，key,value键值对的变量名最好用有意义的，例如:字典中存储的是name,language，那就是name和language
for key, value in alien.items():
    print("键值是"+key+"="*2+">"+str(value))

#   遍历字典中的所有键
#   这种写法易于理解
for key in alien.keys():
    print("键值是" + key)
#   遍历字典中的所有键 与 上面等价
for key in alien:
    print("键值是" + key)

#   遍历字典中的所有键[按顺序]
#   通过sorted函数对字典进行排序并生成一个键列表的副本
for key in sorted(alien):
    print("键值是" + key)

#   遍历字典中的所有值
for value in alien.values():
    print("值是" + str(value))

#   集合 set
#   集合是不重复的列表[唯一性]
#   函数 set() 可以使列表变成 集合
#   定义一个字典
languages = {
    "eric":"ruby",
    "jay":"python",
    "cythia":"ruby",
    "jacky":"java"
}
#   通过set函数去掉value列表的重复值，并遍历value列表
for language in set(languages.values()):
    print("language is " + language)

#   字典中嵌套其他数据集合
#   字典中嵌套字典
users = {
    "jay":{"age":18, "city":"wuxi", "salary":10000},
    "cythia":{"age":16, "city":"wuxi", "salary":8000}
}
print(users)

#   遍历字典中嵌套的字典
for name, content in users.items():
    for key, value in  content.items():
        print( name + " == " + key + "==>" + str(value))

#   指数运算 ** 后根 指数
print(calc_int ** 2)

#   字符串拼接
print(message_str + message2_str)

#   制表符 \t
print(message_str + '\t' + message2_str)

#   换行符 \n
print(message_str + '\n' + message2_str)

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

#   内建函数
#   打印函数
print("Hello,Python World!")

#   首字母大写
#   注意:如果字符串是一句话的情况下，每个单独的词首字母都会大写
print(message_str.title())

#   全部大写
print(message_str.upper())

#   全部小写
print(message_str.lower())

#   字符串右边空白消除
print(message_str.rstrip())

#   字符串左边空白消除
print(message_str.lstrip())

#   字符串两变空白消除
print(message_str.strip())

#   强制转换字符串
print(str(calc_int) + message_str)

#   数据类型
print(type(message_str))
print(type(colors))

#   if条件判断
#   代码案例1
#   if
#   集合中是否存在这个值
if(81 in nums):
    print("the list has a 81")
else:
    print("error")

#   if else
#   集合中是否不存在这个值
if(15 not in nums):
    print("the list has not a 15")
else:
    print("error")

#   if elif else
#   集合中是否存在这些值
if(15 in nums):
    print("15 in the nums")
elif(16 in nums):
    print("16 in the nums")
else:
    print("no nums in the nums")

#   注意: else代码块需要慎用，因为满足条件之外的部分全部执行else代码块中的内容可能引发不可知异常
#   注意: if elif else 代码块在有一个条件满足的情况下，执行完满足条件的代码后直接跳出，下面的条件不会再执行

#   接受输入函数 input()
# username = input("请输入姓名:")
# print(username)

#   while循环
#   代码案例
#   需求: 数数 1 - 5
count = 0
while count < 5:
    count += 1
    print(count)

#   自定义函数
def greet_hello():
    """ 显示 hello """
    print("hello")
greet_hello()

#   自定义函数[带形参]
#   形参: 函数定义时的参数
#   实参: 函数调用时传的参数
#   注意: 形参的位置和实参的位置需要一一对应，否则会出现逻辑错误
#   如果有效的解决在实际调用过程中，实参和形参的位置传递导致的程序逻辑问题，通过使用关键字实参来避免
def  descript_pet(animaltype, animalname):
    print("the animal type is " + animaltype + " and name is " + animalname)
descript_pet("dog","lucky")

#   关键字实参[另一种函数调用方式]
#   是传递给函数的名称=值对
#   不需要考虑形参和实参的位置
#   还可以通过关键字明确值得用途
#   案例代码
descript_pet(animaltype="dog", animalname="lucky")

#   默认参数
#   形参带默认值，这个形参必须写在不带默认值得形参得后面，否则会报错
#   报错原因: 如果不按照上面得位置这么写默认值形参得话，在调用得过程中会出现形参和实参位置问题导致得调用错误
#   调用过程中，如果默认值形参提供了实参传递得话，是直接用实参覆盖默认值
def descipt_pet2(animalname, animaltype = "dog"):
    print("the animal type is " + animaltype + " and name is " + animalname)

#   调用1
descipt_pet2("lucky")
#   调用2
descipt_pet2("lucky","cat")

#   函数返回值
def get_fullname(fistname, lastname):
    return "your full name is " + fistname + "." + lastname

#   返回值函数调用
print(get_fullname("jay","chan"))

#   传递任意数量得实参
#   如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
#   Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
#   * sportname 申明一个空元组
def get_likesports(*sportnames):
    for sportname in sportnames:
        print("sport item is " + sportname)

#   调用任意数量实参得函数
get_likesports("jump","swim","run")
get_likesports("height jump", "drive", "baseketall")

#   位置形参、默认值形参、元组形参, 字典形参混用时应按照如下次序进行排列
#   如按照如下顺序排列: 位置形参、默认值形参、元组形参、字典形参
#   调用函数时，按照位置传递，默认值参数在调用时不能省略
def get_likecolors(name, age = '', *colors, **colorss):
    for color in colors:
        if age:
            print(str(age) + " 's " + name + "is like the " + color)
        else:
            print(name + " is like the " + color)
    print(colorss)
#   调用函数方式1
get_likecolors("jay", "18", "pink","yellow","black", n = "16" , m="15")

#   如按照如下顺序排列: 位置形参、元组形参、默认值形参、字典形参[最佳排列方式]
#   调用函数时，默认值函数通过关键字实参进行传递，可以不考虑位置问题，但是不能放在元组形参前面
def get_likecolors2(name, *colors, age='', **colorss):
    for color in colors:
        if age:
            print(str(age) + " 's " + name + "is like the " + color)
        else:
            print(name + " is like the " + color)
    print(colorss)
#   调用函数方式2
get_likecolors2("jay","pink","yellow","black", age= "18", n = "16" , m="15")
#   调用函数方式3
get_likecolors2("jay","pink","yellow","black",  n = "16" , m="15", age= "18",)

#   导入模板
#   import modulename    modulename.py文件必须与需导入得文件在同一个目录下面
#   在导入文件中使用相关函数，需要通过modulename.functionname()来进行调用

#   导入特定的函数
#   from modulename import functionname1, functionname2, functionname3...
#   在导入文件中使用相关函数，只需要通过functionname1()来进行调用

#   使用as给导入的函数取一个别名
#   from modulename import functionname1 as temp
#   在导入文件中使用导入的函数时，只需要通过temp()进行调用

#   使用as给模块取别名
#   import modulename as temp
#   在导入文件中使用相关函数，需要通过temp.functionname()来进行调用

#   导入模板中所有函数
#   from modulename import *
#   不建议使用，容易因为函数名重名导致不可预测错误


