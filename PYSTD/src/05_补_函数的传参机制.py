# 05_补_函数的传参机制.py
# 2025/1/26   00:42


def f1(my_list):
    my_list[0] = "666"


mylist = ["jack", "mary"]
print(f"f1:{mylist}")  # f1:['jack', 'mary']/
f1(mylist)
print(f"f1修改:{mylist}")  # f1修改:['666', 'mary']0 