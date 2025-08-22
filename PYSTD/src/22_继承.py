# 22_继承.py
# 2025/1/24   22:30

# 继承是面向对象的三大特性之一
# 继承的目的是实现代码的复用
# 继承的实现方式是使用class 子类名(父类名)

# 定义父类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')

# 定义子类
class Dog(Animal):
    def __init__(self, name, age, breed):
        # 调用父类的构造方法
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking.')

    # 重写父类的方法
    def eat(self):
        print(f'{self.name} is eating bones.')

# 定义子类
class Cat(Animal):
    def __init__(self, name, age, color):
        # 调用父类的构造方法
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f'{self.name} is meowing.')

    # 重写父类的方法
    def eat(self):
        print(f'{self.name} is eating fish.')

# 创建对象
dog = Dog('Buddy', 3, 'Golden Retriever')
cat = Cat('Kitty', 2, 'White')

# 调用方法
dog.eat()    # Buddy is eating bones.
dog.sleep()  # Buddy is sleeping.
dog.bark()   # Buddy is barking.

cat.eat()    # Kitty is eating fish.
cat.sleep()  # Kitty is sleeping.
cat.meow()   # Kitty is meowing.

# 判断对象是否是某个类的实例
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Cat))     # False

# 判断类是否是某个类的子类
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False

# 总结：
# 1. 子类继承父类的属性和方法
# 2. 子类可以定义自己的属性和方法
# 3. 子类可以重写父类的方法
# 4. 使用super()调用父类的方法
# 5. isinstance()判断对象是否是某个类的实例
# 6. issubclass()判断类是否是某个类的子类 