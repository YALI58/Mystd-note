# 04_int_detail.py
# 2025/1/15   17:23
import sys

# began'
# python中的整形可以表示很大的数
n3 = 9 ** 888  # 9的888次方
print("n3:   ", n3, type(n3))
# -----------------------------------------------------------
# python的整数有十进制,八进制,十六进制,二进制
print(10)  # 10
# 十六进制
print(0x10)  # 16
# 八进制
print(0o10)  # 8
# 二进制
print(0b10)  # 2

# 字节数随着数字变大而变大,每次增加四个字节
n1 = 0
n2 = 2 ** 8
print("n1:", sys.getsizeof(n1))
print("n2: ", n2, sys.getsizeof(n2)) 