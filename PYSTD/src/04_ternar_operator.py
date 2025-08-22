# 04_ternar_operator.py
# 2025/1/17   15:49

# python 中无三元运算符,可以用if else 关键字

a = 10
b = 80
c=90
max= a if a > b else b if (a if a > b else b)>c else c# 80
# if(max>c):
#     pass
# else:max = c
print(f"max={max}") 