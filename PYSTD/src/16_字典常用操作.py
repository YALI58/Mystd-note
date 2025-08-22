# 16_字典常用操作.py
# 2025/1/24   21:10

# 字典的遍历
# 1) 遍历字典的键
dict_A = {'name': 'tom', 'age': 18, 'gender': '男'}
for key in dict_A.keys():
    print(key)  # name age gender

# 2) 遍历字典的值
for value in dict_A.values():
    print(value)  # tom 18 男

# 3) 遍历字典的键值对
for item in dict_A.items():
    print(item)  # ('name', 'tom') ('age', 18) ('gender', '男')

# 4) 遍历字典的键值对（解包）
for key, value in dict_A.items():
    print(f'{key}={value}')  # name=tom age=18 gender=男

# 字典的判断
# 1) 判断键是否存在
print('name' in dict_A)  # True
print('height' in dict_A)  # False

# 2) 判断值是否存在
print('tom' in dict_A.values())  # True
print('jerry' in dict_A.values())  # False

# 字典的合并
dict_B = {'height': 180, 'weight': 70}
dict_A.update(dict_B)
print(dict_A)  # {'name': 'tom', 'age': 18, 'gender': '男', 'height': 180, 'weight': 70}

# 字典的拷贝
dict_C = dict_A.copy()
print(dict_C)  # {'name': 'tom', 'age': 18, 'gender': '男', 'height': 180, 'weight': 70} 