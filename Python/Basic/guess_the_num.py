from random import random
#   生成随机数后，接受用户输入，判断用户猜的数字是否正确
def guessthenum():
    #   随机生成1-100之间的整数
    guessnum = int(random() * 100)
    #   定义循环变量
    flag = True
    #   循环处理
    while  flag:
        #   判断自动生成的随机数与输入的数字是否相等
        #   相等，提示猜对了
        if guessnum == int(input("请输入猜的数字: ")):
            print("您猜对啦，你真棒！")
            #   设置退出条件
            flag = False
        #   不相等，提示错误
        else:
            print("您猜错了，不好意思，请重新猜")
#   函数调用
# guessthenum()

#
#   自动出题目进行加减乘除法训练
#   第一个参数: 多少位以内的四则运算
#   第二个参数: 取几种计算方法
#   第三个参数: 出多少道题目
#   1、+
#   2、+ -
#   3、+ - *
#   4、+ - * /
def calc_training(numrange, topicnum, topicrange):
    #   定义加减乘除
    func = {"0":"+", "1":"-","2":"*","3":"/"}
    scores = 0
    # print(func[str(int(random() * topicnum))])
    for i in range(1, topicrange):
        #   生成两个随机正整数
        num1 = int(random() * numrange)
        num2 = int(random() * numrange)
        #   随机生成
        if func[str(int(random() * topicnum))] == "+":
            if int(input(str(num1) + " + " + str(num2) + " = ")) == (num1 + num2):
                scores += 100 / topicrange
                continue
        if func[str(int(random() * topicnum))] == "-":
            if int(input(str(num1) + " - " + str(num2) + " = ")) == (num1 - num2):
                scores += 100 / topicrange
                continue
        if func[str(int(random() * topicnum))] == "*":
            if int(input(str(num1) + " * " + str(num2) + " = ")) == (num1 * num2):
                scores += 100 / topicrange
                continue
        if func[str(int(random() * topicnum))] == "/":
            if int(input(str(num1) + " / " + str(num2) + " = ")) == (num1 / num2):
                scores += 100 / topicrange
                continue
    print("您最后的得分是" + str(scores))


# calc_training(20,2,11)

calc_training(10000,4,10)