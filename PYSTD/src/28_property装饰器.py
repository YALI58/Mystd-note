# 28_property装饰器.py
# 2025/1/25   00:00

# property装饰器可以将一个方法转换为属性，使其可以像访问属性一样访问方法
# property装饰器可以实现对属性的访问控制

class Student:
    def __init__(self, name, age):
        self._name = name  # 使用下划线表示私有属性
        self._age = age

    # getter方法
    @property
    def name(self):
        return self._name

    # setter方法
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if len(value) < 2:
            raise ValueError('Name is too short')
        self._name = value

    # getter方法
    @property
    def age(self):
        return self._age

    # setter方法
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be an integer')
        if value < 0 or value > 120:
            raise ValueError('Age must be between 0 and 120')
        self._age = value

    # 只读属性
    @property
    def info(self):
        return f'Name: {self._name}, Age: {self._age}'

# 创建对象
s1 = Student('Tom', 18)

# 访问属性
print(s1.name)  # Tom
print(s1.age)   # 18
print(s1.info)  # Name: Tom, Age: 18

# 修改属性
s1.name = 'Jerry'
s1.age = 20
print(s1.info)  # Name: Jerry, Age: 20

# 异常处理
try:
    s1.name = 'A'  # ValueError: Name is too short
except ValueError as e:
    print(e)

try:
    s1.age = 150  # ValueError: Age must be between 0 and 120
except ValueError as e:
    print(e)

try:
    s1.name = 123  # TypeError: Name must be a string
except TypeError as e:
    print(e)

try:
    s1.age = '20'  # TypeError: Age must be an integer
except TypeError as e:
    print(e)

# 无法修改只读属性
try:
    s1.info = 'New Info'  # AttributeError: can't set attribute
except AttributeError as e:
    print(e)

# 总结：
# 1. property装饰器可以将方法转换为属性
# 2. 使用@property定义getter方法
# 3. 使用@属性名.setter定义setter方法
# 4. 可以在getter和setter方法中添加验证逻辑
# 5. 只定义getter方法的属性是只读属性
# 6. property装饰器可以实现对属性的访问控制
# 7. 可以在setter方法中对属性值进行验证 