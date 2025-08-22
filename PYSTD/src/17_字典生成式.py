# 17_字典生成式.py
# 2025/1/24   21:25

# 字典生成式的语法:
# {key表达式: value表达式 for 变量 in 可迭代对象}

# 示例: 创建一个字典，键是1-5，值是它们的平方
dict_A = {i: i ** 2 for i in range(1, 6)}
print(dict_A)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 示例: 创建一个字典，键是1-10中的偶数，值是它们的平方
dict_B = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(dict_B)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 示例: 将两个列表合并为字典
keys = ['name', 'age', 'gender']
values = ['tom', 18, '男']
dict_C = {keys[i]: values[i] for i in range(len(keys))}
print(dict_C)  # {'name': 'tom', 'age': 18, 'gender': '男'} 