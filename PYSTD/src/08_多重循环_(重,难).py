# 08_多重循环_(重,难).py
# 2025/1/19   19:41
from twisted.python.util import println

for i in range(1,6):
    #  这里end="" 表示输出不换行
    for z in range(6-i-1):
        print(" ",end="")
    for j in range(2*i-1):
             if j==0 or j==2*i-2 or i==5:
                    print("*", end="")
             else:print("-", end="")

    println() 