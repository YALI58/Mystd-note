# 10_ptyhon_continue.py
# 2025/1/19   21:04

# continue语句用于跳过当前循环的剩余语句，然后继续进行下一轮循环
# 基本语法：
# while/for 循环:
#     if 条件:
#         continue
#     循环体

# 示例1：打印1-10之间的奇数
for i in range(1, 11):
    if i % 2 == 0:  # 如果是偶数
        continue  # 跳过本次循环的剩余语句
    print(i, end=" ")  # 只打印奇数

print("\n" + "-" * 20)

# 示例2：while循环中使用continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # 跳过i=3时的打印
    print(f"i={i}")  # 打印除了3以外的数 