# 34_迭代器和生成器.py
# 2025/1/25   01:30

# 迭代器是一个可以记住遍历位置的对象
# 生成器是一种特殊的迭代器，使用yield关键字

# 迭代器
# 实现__iter__和__next__方法的对象就是迭代器
class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

# 使用迭代器
counter = Counter(1, 5)
for num in counter:
    print(num)  # 1 2 3 4

# 生成器函数
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 使用生成器
for num in fibonacci(5):
    print(num)  # 0 1 1 2 3

# 生成器表达式
squares = (x**2 for x in range(5))
for square in squares:
    print(square)  # 0 1 4 9 16

# 无限生成器
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# 使用无限生成器（需要手动停止）
counter = infinite_counter()
for i in range(5):
    print(next(counter))  # 0 1 2 3 4

# 生成器的send方法
def counter_with_send():
    num = 0
    while True:
        val = yield num
        if val is not None:
            num = val
        else:
            num += 1

gen = counter_with_send()
print(next(gen))    # 0
print(gen.send(10)) # 10
print(next(gen))    # 11

# yield from
def sub_gen():
    yield 1
    yield 2
    yield 3

def main_gen():
    yield 'a'
    yield from sub_gen()
    yield 'b'

for item in main_gen():
    print(item)  # a 1 2 3 b

# 迭代器和生成器的应用

# 1. 内存效率
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:  # 文件对象是一个迭代器
            yield line.strip()

# 2. 管道和数据处理
def generate_data():
    for i in range(100):
        yield i

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def multiply_by_two(numbers):
    for num in numbers:
        yield num * 2

# 构建处理管道
numbers = generate_data()
even_numbers = filter_even(numbers)
doubled_numbers = multiply_by_two(even_numbers)

for num in doubled_numbers:
    if num > 50:
        break
    print(num)

# 3. 自定义范围生成器
def custom_range(start, end, step):
    while start < end:
        yield start
        start += step

for num in custom_range(0, 5, 0.5):
    print(f'{num:.1f}')  # 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5

# 总结：
# 1. 迭代器是实现了__iter__和__next__方法的对象
# 2. 生成器是一种特殊的迭代器，使用yield关键字
# 3. 生成器函数返回一个生成器对象
# 4. 生成器表达式类似列表推导式，但使用()
# 5. yield from用于从其他生成器中产生值
# 6. 生成器可以通过send()方法接收值
# 7. 迭代器和生成器可以提高内存效率
# 8. 可以使用生成器构建数据处理管道 