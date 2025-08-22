# 05_for循环_detail.py
# 2025/1/19   15:17

# 基本语法:
# for <变量> in <范围/序列>:
#     <循环操作语句>
# 说明
# 1.for , in 是关键字
# 2.<范围/序列> 可以理解要处理的数据集,需要是可迭代对象(比如字符串,列表)
# 3.循环操作语句,这里可以有多条语句,也就是我们要循环执行的代码
# 4.Python的for循环是一种"轮询机制",是对指定的数据集,进行"轮训处理"

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in "fdabdjk":
    print("你好啊", x)

# for也可以与else 配合{

# for <var> in <sequence>:
    # <statements>
# else: 只执行一次
    # <statements>
#}
for i in range(10):
    print(i)
    if i==3:
        break#当循环中断,else后不执行
else:#只执行一次
    print("循环结束了") 