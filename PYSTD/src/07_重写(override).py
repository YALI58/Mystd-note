# 07_重写(override).py
# 2025/2/3   01:05

# 基本介绍
# 重写又称覆盖(override) 即子类继承父类的属性和方法后 根据业务需要
# 再重新定义 同名的属性或方法

# 示例1：重写父类方法
class Animal:
    def speak(self):
        print("动物发出声音")
    
    def move(self):
        print("动物移动")

class Dog(Animal):
    # 重写speak方法
    def speak(self):
        print("汪汪汪！")
    
    # 重写move方法
    def move(self):
        print("狗狗跑步")

# 测试重写效果
animal = Animal()
dog = Dog()

print("Animal类的方法：")
animal.speak()  # 输出：动物发出声音
animal.move()   # 输出：动物移动

print("\nDog类重写后的方法：")
dog.speak()     # 输出：汪汪汪！
dog.move()      # 输出：狗狗跑步

# 示例2：重写父类方法并调用父类方法
class Bird(Animal):
    def speak(self):
        # 调用父类的方法
        super().speak()
        print("叽叽喳喳！")
    
    def move(self):
        print("鸟儿飞翔")
        # 调用父类的方法
        super().move()

print("\nBird类重写并调用父类方法：")
bird = Bird()
bird.speak()    # 先输出父类的"动物发出声音"，再输出"叽叽喳喳！"
bird.move()     # 先输出"鸟儿飞翔"，再输出父类的"动物移动"

# 重写的注意事项：
# 1. 子类重写父类方法时，方法名必须相同
# 2. 子类重写父类方法时，参数可以不同
# 3. 子类重写父类方法时，可以通过super()调用父类方法
# 4. 重写是面向对象的多态性的体现之一 