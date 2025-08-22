# 11_return.py
# 2025/1/19   21:05

def f1():
    for i in range(1, 5):
        if i == 3:
            # return 就是跳出函数（只能在函数中用）
            return
        print("i=", i)
    print("结束 ")

f1() 