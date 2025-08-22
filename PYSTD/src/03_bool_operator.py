# 03_bool_operator.py
# 2025/1/17   15:27

# 逻辑/布尔运算符
# and   布尔 "与"   and 是一种短路运算符即 x and y 中,若 x 为False,则 x and y 直接返回 x 否则返回 y
# or       布尔 "或"   or 是 一种短路运算符 即 x or y 中,若 x 为True,则 x or y 直接返回 x 否则返回 y
# not    布尔 "非"

# and运算符的使用
# 定义一个成绩变量
score = 10
# 判断成绩是否在60~80之间

if (score >= 60 and score <= 80):
    print("在")
else:
    print("不在") 