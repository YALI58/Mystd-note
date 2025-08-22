# 02_列表list_detail.py
# 2025/1/22   16:20

# 列表的定义[]中括号
list1 = [100, 200, 300, 400, 500]

# 列表上的使用
# list名[索引值]
# 列表的起始索引是0

# 列表的遍历就是将列表中的每一个元素都取出来并进行操作

# while 遍历列表 ,用到内置函数len()

index = 0
while index < len(list1):
    print(list1[index], "  ", end="")  # 100   200   300   400   500
    index += 1

print("")

# for 遍历列表

for i in list1:
    print(f"for遍历:{i}  ", end="")  # for遍历:100  for遍历:200  for遍历:300  for遍历:400  for遍历:500

# 1如果我们需要一个空列表,可以通过[]和list()方式来定义
# 2列表的元素可以有多个,而且数据类型无限制,允许有重复元素,并且是有序的
list2 = [100, "jack", 200, "jack", ["嵌套"]]
# 列表索引必须在指定范围使用

# 索引也可以从尾部开始,最后一个元素的索引为-1,往前一位为-2,以此类推

# 通过列表[索引]=新值 对数据进行更新,使用列表.append(值) 方法来添加元素

a = "sasad"
print(a) # sasad
print(type(a)) # <class 'str'>
a = a.replace("s", "c", )  # 利用复制老字符串来创建新字符串实现65
print(a) # cacad
# list.appen(x) 将x添加到list序列的末尾

# del list[索引] 删除 list[索引]

# 列表是可变序列的特点

list3 = ["qwe", "Da", 1]
list4 = list3
list4[0] = "w"

# 列表指向的地址值不会变,改变只是内部指针所指向的地址值
print(list4)  # ['w', 'Da', 1]
print(list3)  # ['w', 'Da', 1]


# 对列表进行 赋值时 他会给一个地址 这个地址值是固定不变的
# 尽管列表内的值相等 他们地址值也不一样
list_1 = [100, 200]
list_2 = [100, 200]
print(list_2, id(list_2))  # [100, 200] id:1754460014272
print(list_1, id(list_1))  # [100, 200] id:1754459184576
print(list_1 == list_2)  # True
list_1[0] = 300
print(list_2, id(list_2))  # [100, 200] 1754460014272
print(list_1, id(list_1))  # [300, 200] 1754459184576
print(list_1 == list_2)  # False 