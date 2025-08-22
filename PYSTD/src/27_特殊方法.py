# 27_特殊方法.py
# 2025/1/24   23:45

# Python中的特殊方法（魔术方法）是以双下划线开头和结尾的方法
# 这些方法会在特定的情况下被自动调用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 字符串表示形式
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    # 用于调试的字符串表示形式
    def __repr__(self):
        return f'Person("{self.name}", {self.age})'

    # 比较运算符
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    # 长度
    def __len__(self):
        return len(self.name)

    # 调用对象
    def __call__(self, greeting):
        return f'{greeting}, I am {self.name}'

# 创建对象
p1 = Person('Tom', 18)
p2 = Person('Jerry', 20)
p3 = Person('Tom', 18)

# __str__和__repr__
print(str(p1))   # Person(name=Tom, age=18)
print(repr(p1))  # Person("Tom", 18)

# __eq__和__lt__
print(p1 == p3)  # True
print(p1 == p2)  # False
print(p1 < p2)   # True

# __len__
print(len(p1))  # 3

# __call__
print(p1('Hello'))  # Hello, I am Tom

# 其他常用的特殊方法：
# __getitem__: 获取元素，使对象可以像列表一样使用索引
# __setitem__: 设置元素
# __delitem__: 删除元素
class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if index >= len(self.data):
            self.data.extend([None] * (index - len(self.data) + 1))
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __len__(self):
        return len(self.data)

# 使用MyList
my_list = MyList()
my_list[0] = 'a'
my_list[1] = 'b'
my_list[3] = 'd'
print(my_list.data)  # ['a', 'b', None, 'd']
print(my_list[1])    # b
del my_list[1]
print(my_list.data)  # ['a', None, 'd']

# 总结：
# 1. 特殊方法以双下划线开头和结尾
# 2. 特殊方法会在特定情况下自动调用
# 3. __str__用于str()函数和print()函数
# 4. __repr__用于repr()函数和调试
# 5. __eq__和__lt__等用于比较运算
# 6. __len__用于len()函数
# 7. __call__使对象可以像函数一样调用
# 8. __getitem__等使对象可以像序列一样操作 