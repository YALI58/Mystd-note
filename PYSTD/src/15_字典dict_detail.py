# 15_字典dict_detail.py
# 2025/1/24   20:55

# 字典是一种可变序列
# 字典是以键值对的方式存储数据的
# 字典的键必须是不可变对象
# 字典的值可以是任意类型的对象
# 字典中的键是唯一的
# 字典是无序的

# 字典的创建
# 1) 使用{}创建字典
dict_A = {'name': 'tom', 'age': 18}
print(dict_A)  # {'name': 'tom', 'age': 18}

# 2) 使用dict()创建字典
dict_B = dict(name='tom', age=18)
print(dict_B)  # {'name': 'tom', 'age': 18}

# 字典的访问
# 1) 使用[]访问字典中的值
print(dict_A['name'])  # tom

# 2) 使用get()方法访问字典中的值
print(dict_A.get('name'))  # tom

# 字典的添加和修改
# 1) 使用[]添加和修改字典中的键值对
dict_A['gender'] = '男'
print(dict_A)  # {'name': 'tom', 'age': 18, 'gender': '男'}

# 2) 使用update()方法添加和修改字典中的键值对
dict_A.update({'name': 'jerry', 'height': 180})
print(dict_A)  # {'name': 'jerry', 'age': 18, 'gender': '男', 'height': 180}

# 字典的删除
# 1) 使用del删除字典中的键值对
del dict_A['height']
print(dict_A)  # {'name': 'jerry', 'age': 18, 'gender': '男'}

# 2) 使用pop()方法删除字典中的键值对
dict_A.pop('gender')
print(dict_A)  # {'name': 'jerry', 'age': 18}

# 3) 使用clear()方法清空字典
dict_A.clear()
print(dict_A)  # {} 