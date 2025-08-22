# 07_函数作为参数_detail.py
# 2025/1/22   01:31

# 函数作为参数传递,传递的不是数据,而是业务逻辑

def get_max(num1,num2):
    return num2 if num2>num1 else num1

def f1(fun,num1,num2):
    return fun(num1,num2)

def f2(num1,num2):
    return get_max(num1,num2)


print(f2(10, 20))#20

print(f1(get_max, num1=10, num2=20))#20 