# 09_type_change_detail.py
# 2025/1/17   14:41

# int float 都可以转成str
n = 100
m = 100.23
print(str(n))
print(str(m))

# int float互相转化,int变量后会添加.0,float变量会保留整数部分

print(int(m))  # 100
print(float(n))  # 100.0

# str 转int float 使用 int(x) ,float(x)
# 格式不正确,则不能转换
b = "12.3"  # 12.3
v = "holl"
print(float(b))
# print(float(v))  # ValueError

i = 10
j = float(i)
i = j + 1
print(i, type(i))  # 11.0 <class 'float'> 