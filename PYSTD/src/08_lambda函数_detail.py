# 08_lambda函数_detail.py
# 2025/1/22   01:42

# def 关键字,可以定义带有名称的函数,可以重复使用
# lambda 关键字,可以定义匿名函数(无名称),匿名函数只能使用一次

# 基本语法
# lambda 形参列表:函数体(一行代码)

def f1(fun, num1, num2):
    return fun(num1, num2)


f1(lambda a, b: a if a > b else b, num1=10, num2=20)
# 不需要return ，运算结果就是返回值

#lambda函数不能独立存在
lambda a,b:print(a,b) 