# 06_bool_detail.py
# 2025/1/16   15:03

# bool类型的基本使用
num1 = 100
num2 = 200

if num1 < num2:
    print("num1<num2")
result = num1 < num2
print("result: ", result, type(result))  # True   bool

# 布尔类型可以与其他类型进行比较
b1 = True
b2 = False

print(10 + b1)  # 11
print(10 + b2)  # 10

# 在比较时,python会将True视为1,False视为0
if b1 == 1:
    print("ok")
if b2 == 0:
    print("HI")

# 在python中,非0被视为真值,0值被视为假值

if 0:
    print("hh")  # 不输出
if -1:
    print("xx")  # xx 