# 02_compare.py
# 2025/1/17   15:12

#比较运算符的结果要么是True ,要么是False

a=8
b=9
print(a>b)#False
print(a>=b)#False
print(a<b)#True
print(a<=b)#True
print(a==b)#False
print(a!=b)#True

#is 比较运算符 ----> 判断两个变量引用对象是否为同一个
print(a is b)#False
#is not 比较运算符 -----> 判断两个变量引用对象是否不同
print(a is not b)#True 