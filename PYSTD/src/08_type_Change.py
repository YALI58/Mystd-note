# 08_type_Change.py
# 2025/1/16   18:01

# 隐式类型转换
var1 = 10
var2 = 1.2
var3 = var1 + var2
print("var3=", var3, "var3的类型:", type(var3))  # var3= 11.2 var3的类型: <class 'float'>
var1 = var1 + 0.1
print("var1=", var1, "var1的类型:", type(var1))  # var1= 10.1 var1的类型: <class 'float'>

# 显示类型转换
i = 10

j = float(i)
print("j的类型: ", type(j), "j=", j)  # j的类型:  <class 'float'> j= 10.0 