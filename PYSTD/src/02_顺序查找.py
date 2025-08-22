# 02_顺序查找.py
# 2025/1/29   14:31

# 顺序查找（线性查找）是最基本的查找算法
# 从列表第一个元素开始，顺序进行搜索，直到找到目标元素或搜索到列表最后一个元素为止

def sequential_search(lst, key):
    """
    顺序查找算法
    :param lst: 要搜索的列表
    :param key: 要查找的关键字
    :return: 如果找到返回索引，否则返回-1
    """
    for i in range(len(lst)):
        if lst[i] == key:
            return i  # 找到元素，返回索引
    return -1  # 没找到，返回-1

# 测试顺序查找
test_list = [64, 34, 25, 12, 22, 11, 90]
search_key = 22

# 查找元素
result = sequential_search(test_list, search_key)

# 输出结果
if result != -1:
    print(f"元素 {search_key} 在列表中的索引是 {result}")
else:
    print(f"元素 {search_key} 不在列表中")

# 顺序查找的优缺点：
# 优点：
# 1. 算法简单，容易实现
# 2. 对数据的排序状态没有要求
# 3. 对数据的存储结构没有要求

# 缺点：
# 1. 查找效率低，时间复杂度为O(n)
# 2. 当n很大时，平均查找长度较大 