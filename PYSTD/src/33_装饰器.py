# 33_装饰器.py
# 2025/1/25   01:15

# 装饰器是一种函数，它可以在不修改原函数的情况下扩展其功能
# 装饰器是Python面向切面编程（AOP）的一种实现

import time
import functools

# 基本装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.2f} seconds to run')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print('Function executed')

slow_function()

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        @functools.wraps(func)  # 保留原函数的元信息
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')

# 类装饰器
class Logger:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)  # 保留原函数的元信息

    def __call__(self, *args, **kwargs):
        print(f'Calling {self.func.__name__}')
        result = self.func(*args, **kwargs)
        print(f'{self.func.__name__} finished')
        return result

@Logger
def test_function():
    print('Function is running')

test_function()

# 多个装饰器
def bold(func):
    @functools.wraps(func)
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper():
        return f'<i>{func()}</i>'
    return wrapper

@bold
@italic
def hello():
    return 'Hello, World!'

print(hello())  # <b><i>Hello, World!</i></b>

# 装饰器的应用场景

# 1. 记录日志
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

# 2. 性能测试
def performance_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import cProfile
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.print_stats()
        return result
    return wrapper

# 3. 访问控制
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 这里应该有认证逻辑
        is_authenticated = True
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            raise Exception('Authentication required')
    return wrapper

# 4. 缓存
def cache(func):
    cached_results = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 使用缓存的斐波那契数列计算

# 总结：
# 1. 装饰器是一种函数，用于扩展其他函数的功能
# 2. 装饰器可以带参数
# 3. 可以使用类作为装饰器
# 4. 可以同时使用多个装饰器
# 5. functools.wraps用于保留原函数的元信息
# 6. 装饰器常用于日志、性能测试、访问控制等场景
# 7. 装饰器是Python中重要的设计模式之一 