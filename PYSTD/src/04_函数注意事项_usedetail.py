# 04_函数注意事项_usedetail.py
# 2025/1/20   16:41

# 函数的变量是局部的,在函数外不能使用

# 如果同一个文件,出现两个函数名相同的函数,则以就近原则进行调用

def cry():
    print("ok,hi")


def cry():
    print("hi,ok")


cry()  # hi,ok


# 调用函数时,根据函数定义的参数位置来传递参数,这种传参方式就是位置参数,
# 传递的实参和定义的形参顺序和个数必须一致,同时定义的形参,不用指定数据类型
# 会根据传入的实参决定

# 函数可以有多个返回值
# 比如函数接收两个数,返回这两个数的和,,差
def f2(n1, n2):
    print("关键字参数可以改顺序")
    return n1 + n2, n1 - n2


r1, r2 = f2(30, 40)
print(f"r1->{r1},r2->{r2}")  # r1->70,r2->-10

# 关键字参数
f2(n2=30, n1=10)


# 函数支持默认参数/缺省参数
# 定义函数时,可以给参数提供默认值,调用函数时,指定了实参,则以指定为准，没有指定，则以默认值为准
# 默认参数,需要放在参数列表后,不然会报错
def book_info(name="默认参数", age=18, ):
    print(f"name={name},age={age}")


book_info()


# 函数支持可变参数/不定长参数
# 传入的可变参数会以元组的形式存储

def sum(*args):
    print(f"args->{args}类型是:{type(args)}")  # args->(1, 2, 3, 100)类型是:<class 'tuple'>
    total = 0
    # 对args进行遍历,即对元组遍历
    for element in args:
        total = element + total
    return total


tot = sum(1, 2, 3, 100)
print(tot)  # 106


# 函数的可变参数,还支持多个关键字参数,也就是多个"形参名=实参值"
# 传入的多个关键字参数,会组成一部字典(dict)

# 比如我们要接收一个人的信息
def person_info(**args):
    print(f"args->{args}类型->{type(args)}")
    # args[args_key]就是取出参数值
    for args_key in args:
        print(f"参数名->{args_key} 参数值->{args[args_key]}")


person_info(name="小王", age=18, gender="男")

# python调用另一个.py文件的函数
# 导入f1.py这个模块
import f1
f1.f1()


# 方括号 [] 用于表示函数或方法的参数是可选的
# class range(start, stop[, step])
# [,step]是可选参数的意思,可以传参也可以不传 