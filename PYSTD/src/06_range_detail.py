# 06_range_detail.py
# 2025/1/19   17:11

# range函数的解读
# class  range(stop)
# class  range(start,stop,step=1)
# 虽然被称为函数,但range 实际上是一个不可变的序列类型
# range 默认增加的步长step是1,也可以指定,start默认是0
# 通过list() 可以查看range()生成的序列包含的数据
# range生成的数列是前闭后开 range(1,5)

# r1 = range(1, 6, 1)
r1 = range(1,6)
print(r1)  # range(1,6)
print(list(r1)) 