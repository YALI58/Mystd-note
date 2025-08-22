# 03_list列表常用操作.py
# 2025/1/23   15:05

# 函数
# len(list)
# max(list)
# min(list)
# list(seq):将元祖转换为列表

list_a = [100, 200, 300, 400, 500]
print("列表的元素个数:", len(list_a))
print("列表的最大元素:", max(list_a))
print("列表的最小元素:", min(list_a))

# list.append(obj) :  在列表末尾添加新的对象
list_a.append(100)
print(list_a)  # [100, 200, 300, 400, 500, 100]

# list.count(obj)  :   统计某个元素在列表中出现的次数
print("100出现的次数:", list_a.count(100))  # 100出现的次数: 2

# list.extend(seq): 在列表的末尾一次性追加另一个序列中的多个值(用新列表拓展原来的列表)
list_b = [1, 2, 3]
list_a.extend(list_b)
print(list_a)  # [100, 200, 300, 400, 500, 100, 1, 2, 3]

# list.index(obj) : 从列表中找出某个值第一个匹配项的索引位置
# 如果找不到,会报错
print(list_a.index(100))  # 0
# print(list_a.index(600))  # ValueError: 600 is not in list

# 翻转list  list.reverse()
list_a.reverse()
print(list_a)  # [3, 2, 1, 100, 500, 400, 300, 200, 100]

#   list.insert(index,obj)        在任意位置插入元素
list_a.insert(0, 6)
print(list_a)  # [6, 3, 2, 1, 100, 500, 400, 300, 200, 100] 