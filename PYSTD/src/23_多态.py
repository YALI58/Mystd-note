# 23_多态.py
# 2025/1/24   22:45

# 多态是面向对象的三大特性之一
# 多态的目的是提高代码的灵活性和可扩展性
# 多态的实现方式是通过继承和方法重写

# 定义父类
class Animal:
    def speak(self):
        pass

# 定义子类
class Dog(Animal):
    def speak(self):
        print('Dog says: Woof!')

# 定义子类
class Cat(Animal):
    def speak(self):
        print('Cat says: Meow!')

# 定义子类
class Duck(Animal):
    def speak(self):
        print('Duck says: Quack!')

# 定义函数，接收Animal类型的参数
def animal_speak(animal):
    animal.speak()

# 创建对象
dog = Dog()
cat = Cat()
duck = Duck()

# 调用函数
animal_speak(dog)   # Dog says: Woof!
animal_speak(cat)   # Cat says: Meow!
animal_speak(duck)  # Duck says: Quack!

# 多态的好处：
# 1. 增加新的动物类型时，不需要修改animal_speak函数
# 2. animal_speak函数可以处理所有继承自Animal的类的对象
# 3. 提高了代码的可扩展性和灵活性

# 示例：新增一个动物类型
class Cow(Animal):
    def speak(self):
        print('Cow says: Moo!')

# 创建对象并调用函数
cow = Cow()
animal_speak(cow)  # Cow says: Moo!

# 总结：
# 1. 多态是一种运行时的特性
# 2. 多态通过继承和方法重写实现
# 3. 多态提高了代码的灵活性和可扩展性
# 4. 多态使得代码更加简洁和易于维护 