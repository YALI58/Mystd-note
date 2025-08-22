# 20_类和对象.py
# 2025/1/24   22:00

# 类是对象的模板，对象是类的实例
# 类中的函数称为方法，类中的变量称为属性

# 定义类
class Person:
    # 类属性
    count = 0

    # 构造方法
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        Person.count += 1

    # 实例方法
    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old.')

    # 类方法
    @classmethod
    def get_count(cls):
        return cls.count

    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 创建对象
p1 = Person('Tom', 18)
p2 = Person('Jerry', 20)

# 调用实例方法
p1.say_hello()  # Hello, my name is Tom, I am 18 years old.
p2.say_hello()  # Hello, my name is Jerry, I am 20 years old.

# 访问类属性
print(Person.count)  # 2

# 调用类方法
print(Person.get_count())  # 2

# 调用静态方法
print(Person.is_adult(18))  # True
print(Person.is_adult(16))  # False

# 总结：
# 1. 类是创建对象的模板
# 2. 对象是类的实例
# 3. 类中的函数称为方法
# 4. 类中的变量称为属性
# 5. 实例方法第一个参数是self，代表当前对象
# 6. 类方法第一个参数是cls，代表当前类
# 7. 静态方法不需要特殊参数
# 8. 类属性属于类，实例属性属于对象 