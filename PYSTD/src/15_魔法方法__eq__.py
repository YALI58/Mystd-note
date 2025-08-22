# 15_魔法方法__eq__.py
# 2025/2/3   22:07

# 没有重写 __eq__前, == 比较的是内存地址
# 重写__eq__方法后，可以自定义对象之间的相等比较规则

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 不重写__eq__时，比较的是对象的内存地址
    # 即使坐标相同的两个点也会被认为是不相等的

class Point2D(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    # 重写__eq__方法，定义两个点相等的条件是坐标相同
    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # 重写__eq__方法，定义两个矩形相等的条件是面积相同
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width * self.height == other.width * other.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# 测试未重写__eq__的Point类
p1 = Point(1, 2)
p2 = Point(1, 2)
print("未重写__eq__的Point类：")
print(f"p1 == p2: {p1 == p2}")  # False，比较的是内存地址

# 测试重写__eq__后的Point2D类
p3 = Point2D(1, 2)
p4 = Point2D(1, 2)
p5 = Point2D(2, 3)
print("\n重写__eq__后的Point2D类：")
print(f"p3 == p4: {p3 == p4}")  # True，坐标相同
print(f"p3 == p5: {p3 == p5}")  # False，坐标不同

# 测试重写__eq__后的Rectangle类
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 2)
r3 = Rectangle(2, 4)
print("\n重写__eq__后的Rectangle类：")
print(f"{r1} == {r2}: {r1 == r2}")  # True，面积相同（6）
print(f"{r1} == {r3}: {r1 == r3}")  # False，面积不同（6 != 8）

# __eq__方法的特点：
# 1. 用于定义对象之间使用==运算符比较的行为
# 2. 如果不重写，默认比较对象的内存地址
# 3. 重写时应考虑比较对象类型的一致性
# 4. 返回值应该是布尔类型（True或False）
# 5. 实现时应该考虑比较的对称性（a==b 应该与 b==a 结果一致） 