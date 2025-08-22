# 14_魔法方法__str__.py
# 2025/2/3   21:06

# 打印对象默认返回: 类型名+对象内存地址
# 重写__str__方法,print(对象)或str(对象)时,都会自动调用该对象的__str__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 不重写__str__时的默认输出
    # 输出格式类似：<__main__.Person object at 0x00000123456789>

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    # 重写__str__方法
    def __str__(self):
        return f"学生信息：[姓名：{self.name}, 年龄：{self.age}, 学号：{self.student_id}]"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    # 重写__str__方法，返回不同的格式
    def __str__(self):
        return f"教师[{self.name}] - 年龄：{self.age}，教授科目：{self.subject}"

# 测试不同类的__str__方法
person = Person("张三", 25)
student = Student("李四", 18, "2025001")
teacher = Teacher("王老师", 35, "Python编程")

print("未重写__str__的Person类：")
print(person)  # 输出默认的对象表示

print("\n重写__str__后的Student类：")
print(student)  # 输出自定义的学生信息格式

print("\n重写__str__后的Teacher类：")
print(teacher)  # 输出自定义的教师信息格式

# __str__方法的特点：
# 1. 返回值必须是字符串类型
# 2. 当print(对象)时会自动调用
# 3. 当str(对象)时会自动调用
# 4. 用于对象的字符串表示，应该尽量简洁明了
# 5. 如果没有重写__str__，则会使用object类的默认实现 