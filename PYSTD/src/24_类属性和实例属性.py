# 24_类属性和实例属性.py
# 2025/1/24   23:00

# 类属性是属于类的属性，被所有实例共享
# 实例属性是属于实例的属性，每个实例都有独立的实例属性

class Student:
    # 类属性
    school = 'Python School'
    count = 0

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        # 通过类名访问类属性
        Student.count += 1

    def show_info(self):
        # 通过self访问实例属性
        # 通过类名或self访问类属性
        print(f'Name: {self.name}, Age: {self.age}, School: {self.school}')

# 创建对象
s1 = Student('Tom', 18)
s2 = Student('Jerry', 20)

# 访问实例属性
print(s1.name)  # Tom
print(s2.name)  # Jerry

# 访问类属性
print(Student.school)  # Python School
print(s1.school)      # Python School
print(s2.school)      # Python School

# 修改类属性
Student.school = 'New Python School'
print(s1.school)  # New Python School
print(s2.school)  # New Python School

# 统计学生人数
print(Student.count)  # 2

# 注意：通过实例修改类属性实际上是创建了一个同名的实例属性
s1.school = 'My School'
print(Student.school)  # New Python School
print(s1.school)      # My School
print(s2.school)      # New Python School

# 总结：
# 1. 类属性属于类，被所有实例共享
# 2. 实例属性属于实例，每个实例都有独立的实例属性
# 3. 类属性可以通过类名或实例访问
# 4. 实例属性只能通过实例访问
# 5. 通过类名修改类属性会影响所有实例
# 6. 通过实例修改类属性实际上是创建了一个同名的实例属性 