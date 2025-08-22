# 05_float_detail.py
# 2025/1/16   14:14

import sys

# 浮点类型的表现形式

n1 = 5.12
n2 = .12
print(n1)  # 5.12
print(n2)  # 0.12

# 科学计数法形式

n3 = 5.12e2  # 5.12乘以10的2次方
print(n3)  # 512.0
n4 = 5.12e-2  # 5.12除于10的2次方
print(n4)  # 0.0512
print(sys.float_info)  # 浮点型的范围

# 浮点类型计算后,存在精度的损失,可以使用Decimal类进行解决

from decimal import Decimal

a = 8.1 / 2.7
print(a)  # 2.9999999999999996
b = Decimal("8.1") / Decimal("2.7")
print(b)  # 3

# 保留几位小数 可以用format()
c = format(a, ".2f")
print(c)  # 3.00
# 还可以用"%.2f"%变量
d = "%.2f" % a
print(d)  # 3.00 