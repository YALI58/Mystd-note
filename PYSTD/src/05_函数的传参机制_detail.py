# 05_函数的传参机制_detail.py
# 2025/1/20   23:29

# 变量与字符串的传参
# python的驻留机制使地址传递发生值不改变
# 类比于java中的形参实参

def f1(a):
    a += 1
    print(f"id中是{id(a)}a->{a}")

a = 10
print(f"id前是{id(a)}a->{a}")
f1(a)
print(f"f1HOU：id是{id(a)}a->{a}")

def f2(name):
    name+="hi"
    print(f"name中:{id(name)},{name}")

name ="渣想"
print(f"name前:{id(name)},{name}")
f2(name)
print(f"name后:{id(name)},{name}") 