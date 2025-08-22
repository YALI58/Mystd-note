# 09_字符串常用操作.py
# 2025/1/24   00:54

# str.split(seq=None,maxspilt=-1)返回的是一个列表
# 以seq为分隔符
# 若给出了maxspilt,则拆分元素个数最多为maxspilt+1
# 若未给则默认maxspilt=-1并进行所有可能的拆分
str_B = "jacky,tom"
str_A = str_B.split(",")
print(str_A, type(str_A))  # ['jacky', 'tom']，<class 'list'>

str_C = "jack,ab,kong"
print(len(str_C))  # 12

# str.replace(_old,_new,_count)
str_D = str_C.replace("jack", "杰克")
print(str_D)  # 杰克,ab,kong

# str.index(_sub,_start,_end)
str_E = "jack tom bob mark tom"
print(str_E.index("tom"))  # 5
print(str_E.index("tom", 0, 10))  # 5

# str.strip([chars])  :  返回原字符串的副本,去掉前置和后导, chars为要去掉的字符串
str_F = "123tom213"
str_F_strip = str_F.strip("123")
print(str_F_strip)  # tom 