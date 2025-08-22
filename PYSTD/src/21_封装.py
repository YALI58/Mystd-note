# 21_封装.py
# 2025/1/24   22:15

# 封装是面向对象的三大特性之一
# 封装的目的是保护数据和方法的安全性
# 封装的实现方式是使用私有属性和私有方法

# 定义类
class Person:
    def __init__(self, name, age):
        # 私有属性（以双下划线开头）
        self.__name = name
        self.__age = age

    # 私有方法（以双下划线开头）
    def __say_secret(self):
        print('This is a secret.')

    # 公有方法
    def say_hello(self):
        print(f'Hello, my name is {self.__name}, I am {self.__age} years old.')
        self.__say_secret()

    # getter方法
    def get_name(self):
        return self.__name

    # setter方法
    def set_name(self, name):
        if len(name) >= 2:
            self.__name = name
        else:
            print('Name is too short.')

# 创建对象
p1 = Person('Tom', 18)

# 调用公有方法
p1.say_hello()  # Hello, my name is Tom, I am 18 years old.
                # This is a secret.

# 无法直接访问私有属性和私有方法
# print(p1.__name)  # AttributeError
# p1.__say_secret()  # AttributeError

# 使用getter和setter方法访问和修改私有属性
print(p1.get_name())  # Tom
p1.set_name('Jerry')
print(p1.get_name())  # Jerry
p1.set_name('A')  # Name is too short.

# 总结：
# 1. 私有属性和私有方法以双下划线开头
# 2. 私有属性和私有方法只能在类内部访问
# 3. 可以通过公有方法访问私有属性和私有方法
# 4. 可以使用getter和setter方法访问和修改私有属性
# 5. getter和setter方法可以对数据进行验证 