# 19_深浅拷贝.py
# 2025/1/24   21:45

# 浅拷贝：只拷贝第一层数据，不会拷贝更深层次的数据
# 深拷贝：会拷贝所有层次的数据

# 浅拷贝示例
import copy

list_A = [1, 2, [3, 4]]
list_B = list_A.copy()  # 浅拷贝
list_B[2][0] = 5
print(list_A)  # [1, 2, [5, 4]]
print(list_B)  # [1, 2, [5, 4]]

# 深拷贝示例
list_C = [1, 2, [3, 4]]
list_D = copy.deepcopy(list_C)  # 深拷贝
list_D[2][0] = 5
print(list_C)  # [1, 2, [3, 4]]
print(list_D)  # [1, 2, [5, 4]]

# 赋值操作
list_E = [1, 2, [3, 4]]
list_F = list_E  # 赋值操作
list_F[2][0] = 5
print(list_E)  # [1, 2, [5, 4]]
print(list_F)  # [1, 2, [5, 4]]

# 总结：
# 1. 赋值操作是将变量指向同一个对象
# 2. 浅拷贝是创建一个新对象，但只拷贝第一层数据
# 3. 深拷贝是创建一个新对象，并且递归拷贝所有层次的数据 