# 08_字符串str使用_detail.py
# 2025/1/24   00:29

# 字符串是字符的容器
# 字符串支持索引

str_A = "Red,green"

print(f"str_A的第三个字符:{str_A[2]},字符的类型:{type(str_A[2])}")
# 运行结果:
# str_A的第三个字符:d,字符的类型:<class 'str'>

# 快速分隔行写法
print("*" * 30)

# 字符串的遍历
x = 0
for i in str_A:
    print(f"str_A[{x}]:{i}")
    x += 1

# 字符串是不可变序列，不能修改

# 每一个字符串指向的地址都不同
str_B = "abc"
print(f"TheFirst:{id(str_B)}")  # TheFirst:140731553104976
str_B = "abcd"
print(f"TheSecond:{id(str_B)}")  # TheSecond:2202767316400 