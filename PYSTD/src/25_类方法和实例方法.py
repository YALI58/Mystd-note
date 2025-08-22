# 25_类方法和实例方法.py
# 2025/1/24   23:15

# 类方法是属于类的方法，使用@classmethod装饰器
# 实例方法是属于实例的方法，第一个参数是self
# 静态方法使用@staticmethod装饰器，不需要特殊参数

class Student:
    # 类属性
    school = 'Python School'
    count = 0

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        Student.count += 1

    # 实例方法
    def show_info(self):
        print(f'Name: {self.name}, Age: {self.age}, School: {self.school}')

    # 类方法
    @classmethod
    def show_school(cls):
        print(f'School: {cls.school}, Student Count: {cls.count}')

    # 类方法
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 创建对象
s1 = Student('Tom', 18)
s2 = Student('Jerry', 20)

# 调用实例方法
s1.show_info()  # Name: Tom, Age: 18, School: Python School
s2.show_info()  # Name: Jerry, Age: 20, School: Python School

# 调用类方法
Student.show_school()  # School: Python School, Student Count: 2
Student.change_school('New Python School')
Student.show_school()  # School: New Python School, Student Count: 2

# 通过实例调用类方法
s1.show_school()  # School: New Python School, Student Count: 2

# 调用静态方法
print(Student.is_adult(18))  # True
print(Student.is_adult(16))  # False

# 通过实例调用静态方法
print(s1.is_adult(18))  # True
print(s1.is_adult(16))  # False

# 总结：
# 1. 实例方法第一个参数是self，代表当前实例
# 2. 类方法使用@classmethod装饰器，第一个参数是cls，代表当前类
# 3. 静态方法使用@staticmethod装饰器，不需要特殊参数
# 4. 实例方法可以访问实例属性和类属性
# 5. 类方法只能访问类属性，不能访问实例属性
# 6. 静态方法不能访问实例属性和类属性
# 7. 实例方法、类方法和静态方法都可以通过类或实例调用 