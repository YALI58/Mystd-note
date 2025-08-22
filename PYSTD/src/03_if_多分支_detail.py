# 03_if_多分支_detail.py
# 2025/1/19   14:28

# if 条件表达式1:
#     执行代码块1
# elif 条件表达式2:
#     执行代码块2
# ......
# else:
# 执行代码块n+1
x=1
if x<100:
    print(1)
elif x<50:
    print(2)

score = int(input("请输入成绩:"))
if score<60:
    print("不及格")
elif 100 > score > 90:
    print("优秀")
else:
    print("及格")

high = int(input("高:"))
weigh = int(input("富:"))
face = input("帅:")

if high >=180 and weigh>=1000 and face =="帅":
    print("一定嫁")
elif high <180 and weigh<1000 and face !="帅":
    print("不嫁")
else:
    print("嫁吧,比上不足比下有余") 