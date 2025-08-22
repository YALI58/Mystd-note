# 29_异常处理.py
# 2025/1/25   00:15

# 异常处理可以防止程序因为错误而崩溃
# Python使用try-except语句处理异常

# 基本的异常处理
try:
    num = int(input('Enter a number: '))
    result = 10 / num
    print(f'Result: {result}')
except ValueError:
    print('Please enter a valid number')
except ZeroDivisionError:
    print('Cannot divide by zero')

# 处理多个异常
try:
    file = open('nonexistent.txt')
    content = file.read()
    file.close()
except FileNotFoundError:
    print('File not found')
except IOError:
    print('Error reading file')

# 使用else子句
try:
    num = int(input('Enter a positive number: '))
    if num <= 0:
        raise ValueError('Number must be positive')
except ValueError as e:
    print(f'Error: {e}')
else:
    print(f'You entered: {num}')

# 使用finally子句
try:
    file = open('test.txt', 'w')
    file.write('Hello, World!')
except IOError:
    print('Error writing to file')
finally:
    file.close()  # 无论是否发生异常，都会执行

# 自定义异常
class AgeError(Exception):
    def __init__(self, message):
        self.message = message

def set_age(age):
    if age < 0 or age > 120:
        raise AgeError('Age must be between 0 and 120')
    return age

# 使用自定义异常
try:
    age = set_age(150)
except AgeError as e:
    print(f'Error: {e.message}')

# 异常的传递
def func1():
    return 1 / 0

def func2():
    return func1()

def func3():
    try:
        return func2()
    except ZeroDivisionError:
        print('Caught division by zero error')

func3()  # Caught division by zero error

# with语句（上下文管理器）
with open('test.txt', 'r') as file:
    content = file.read()
    # 文件会自动关闭，即使发生异常

# 总结：
# 1. try-except用于捕获和处理异常
# 2. 可以捕获多个异常
# 3. else子句在没有异常时执行
# 4. finally子句总是执行
# 5. 可以自定义异常类
# 6. 异常会沿着调用栈向上传递
# 7. with语句可以自动管理资源 