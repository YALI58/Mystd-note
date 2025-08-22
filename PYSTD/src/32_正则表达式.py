# 32_正则表达式.py
# 2025/1/25   01:00

# 正则表达式是一种用于匹配字符串模式的强大工具
# Python通过re模块提供对正则表达式的支持

import re

# 基本匹配
text = 'Hello, Python!'
pattern = 'Python'
result = re.search(pattern, text)
print(result.group())  # Python

# 使用元字符
# . 匹配任意字符（除了换行符）
# ^ 匹配开头
# $ 匹配结尾
# * 匹配0次或多次
# + 匹配1次或多次
# ? 匹配0次或1次
# {n} 匹配n次
# {n,} 匹配n次或更多次
# {n,m} 匹配n到m次

# 示例
text = 'python python3 python3.7'
pattern = 'python\d*\.?\d*'
result = re.findall(pattern, text)
print(result)  # ['python', 'python3', 'python3.7']

# 字符类
# [abc] 匹配a、b或c
# [^abc] 匹配除了a、b和c的任意字符
# [a-z] 匹配任意小写字母
# [A-Z] 匹配任意大写字母
# [0-9] 匹配任意数字
# \d 匹配任意数字，等同于[0-9]
# \D 匹配任意非数字
# \w 匹配字母、数字、下划线
# \W 匹配非字母、数字、下划线
# \s 匹配任意空白字符
# \S 匹配任意非空白字符

# 示例
text = 'abc123DEF_!@#'
print(re.findall(r'\d+', text))    # ['123']
print(re.findall(r'[a-z]+', text)) # ['abc']
print(re.findall(r'\W+', text))    # ['!@#']

# 分组
text = 'John Smith, Jane Doe'
pattern = r'(\w+)\s(\w+)'
result = re.findall(pattern, text)
print(result)  # [('John', 'Smith'), ('Jane', 'Doe')]

# 替换
text = 'Hello, World!'
pattern = r'World'
replacement = 'Python'
result = re.sub(pattern, replacement, text)
print(result)  # Hello, Python!

# 分割
text = 'apple,banana;orange grape'
pattern = r'[,;\s]'
result = re.split(pattern, text)
print(result)  # ['apple', 'banana', 'orange', 'grape']

# 常用函数
# re.match(): 从字符串开头匹配
# re.search(): 在字符串中查找匹配
# re.findall(): 找到所有匹配
# re.finditer(): 找到所有匹配，返回迭代器
# re.sub(): 替换匹配的文本
# re.split(): 分割字符串

# 编译正则表达式
pattern = re.compile(r'\d+')
text = 'abc123def456'
result = pattern.findall(text)
print(result)  # ['123', '456']

# 贪婪匹配和非贪婪匹配
text = '<p>First</p><p>Second</p>'
print(re.findall(r'<p>.*</p>', text))    # ['<p>First</p><p>Second</p>']
print(re.findall(r'<p>.*?</p>', text))   # ['<p>First</p>', '<p>Second</p>']

# 实际应用示例
# 匹配邮箱
email = 'user@example.com'
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print(re.match(pattern, email) is not None)  # True

# 匹配电话号码
phone = '123-456-7890'
pattern = r'\d{3}-\d{3}-\d{4}'
print(re.match(pattern, phone) is not None)  # True

# 总结：
# 1. 正则表达式是强大的字符串匹配工具
# 2. Python通过re模块支持正则表达式
# 3. 常用元字符：. ^ $ * + ? {} [] \d \w \s
# 4. 常用函数：match search findall sub split
# 5. 可以使用compile()编译正则表达式
# 6. 贪婪匹配和非贪婪匹配的区别
# 7. 正则表达式在实际应用中非常有用 