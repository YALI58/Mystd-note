# 18_推导式总结.py
# 2025/1/24   21:35

# 列表推导式
# [表达式 for 变量 in 可迭代对象]
list_A = [i ** 2 for i in range(1, 6)]
print(list_A)  # [1, 4, 9, 16, 25]

# 集合推导式
# {表达式 for 变量 in 可迭代对象}
set_A = {i ** 2 for i in range(1, 6)}
print(set_A)  # {1, 4, 9, 16, 25}

# 字典推导式
# {key表达式: value表达式 for 变量 in 可迭代对象}
dict_A = {i: i ** 2 for i in range(1, 6)}
print(dict_A)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 带条件的推导式
# [表达式 for 变量 in 可迭代对象 if 条件]
list_B = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(list_B)  # [4, 16, 36, 64, 100]

# 多层推导式
# [表达式 for 变量1 in 可迭代对象1 for 变量2 in 可迭代对象2]
list_C = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list_C)  # [(1, 1), (1, 2), (2, 1), (2, 2)] 