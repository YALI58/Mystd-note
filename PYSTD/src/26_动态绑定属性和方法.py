# 26_动态绑定属性和方法.py
# 2025/1/24   23:30

# Python是动态语言，可以在运行时动态地给类或实例绑定属性和方法

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

# 创建对象
s1 = Student('Tom', 18)
s2 = Student('Jerry', 20)

# 动态绑定实例属性
s1.gender = 'Male'
print(s1.gender)  # Male
# print(s2.gender)  # AttributeError: 'Student' object has no attribute 'gender'

# 定义一个方法
def set_grade(self, grade):
    self.grade = grade

# 动态绑定实例方法
import types
s1.set_grade = types.MethodType(set_grade, s1)
s1.set_grade('A')
print(s1.grade)  # A
# s2.set_grade('B')  # AttributeError: 'Student' object has no attribute 'set_grade'

# 动态绑定类属性
Student.school = 'Python School'
print(Student.school)  # Python School
print(s1.school)      # Python School
print(s2.school)      # Python School

# 动态绑定类方法
@classmethod
def show_school(cls):
    print(f'School: {cls.school}')

Student.show_school = show_school
Student.show_school()  # School: Python School
s1.show_school()      # School: Python School
s2.show_school()      # School: Python School

# 使用__slots__限制实例属性
class Teacher:
    __slots__ = ('name', 'age')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

t1 = Teacher('Mr. Wang', 35)
# t1.gender = 'Male'  # AttributeError: 'Teacher' object has no attribute 'gender'

# 总结：
# 1. 可以动态地给实例绑定属性和方法
# 2. 给实例绑定的属性和方法只对当前实例有效
# 3. 可以动态地给类绑定属性和方法
# 4. 给类绑定的属性和方法对所有实例都有效
# 5. 使用__slots__可以限制实例能添加的属性 