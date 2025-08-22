# 30_模块和包.py
# 2025/1/25   00:30

# 模块是一个包含Python代码的文件
# 包是一个包含多个模块的目录，必须包含__init__.py文件

# 导入模块的方式
import math  # 导入整个模块
print(math.pi)  # 3.141592653589793

from math import sqrt  # 导入特定的函数
print(sqrt(16))  # 4.0

from math import *  # 导入所有内容（不推荐）
print(cos(0))  # 1.0

import math as m  # 使用别名
print(m.pi)  # 3.141592653589793

from math import pi as PI  # 为导入的内容使用别名
print(PI)  # 3.141592653589793

# 创建自己的模块
# 假设有一个名为mymath.py的文件：
"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

PI = 3.14
"""

# 导入自定义模块
# import mymath
# print(mymath.add(10, 5))  # 15
# print(mymath.PI)  # 3.14

# 包的结构示例：
"""
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
        module4.py
"""

# 导入包中的模块
# import mypackage.module1
# from mypackage.subpackage import module3
# from mypackage.subpackage.module4 import function1

# 模块的搜索路径
import sys
print(sys.path)  # 显示模块搜索路径

# 常用的标准库模块
import os  # 操作系统接口
print(os.getcwd())  # 获取当前工作目录

import datetime  # 日期和时间
print(datetime.datetime.now())  # 获取当前时间

import random  # 随机数
print(random.randint(1, 10))  # 生成1-10之间的随机整数

import json  # JSON数据处理
data = {'name': 'Tom', 'age': 18}
json_str = json.dumps(data)
print(json_str)  # {"name": "Tom", "age": 18}

# __name__变量
if __name__ == '__main__':
    print('This module is being run directly')
else:
    print('This module has been imported')

# 总结：
# 1. 模块是一个Python文件
# 2. 包是一个包含多个模块的目录
# 3. 可以使用import导入模块
# 4. 可以使用from...import导入特定内容
# 5. 可以使用as给导入的内容起别名
# 6. 包必须包含__init__.py文件
# 7. sys.path包含模块搜索路径
# 8. Python有丰富的标准库模块
# 9. __name__变量用于判断模块是否被直接运行 