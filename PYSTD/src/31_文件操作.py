# 31_文件操作.py
# 2025/1/25   00:45

# 文件操作包括文件的打开、读取、写入和关闭
# Python提供了内置的open()函数来操作文件

# 打开文件的模式：
# 'r': 只读模式（默认）
# 'w': 写入模式（会覆盖原有内容）
# 'a': 追加模式
# 'b': 二进制模式
# '+': 读写模式

# 写入文件
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('Python is awesome!\n')
    
    # 写入多行
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)

# 读取文件
with open('test.txt', 'r', encoding='utf-8') as file:
    # 读取整个文件
    content = file.read()
    print('全部内容：')
    print(content)

# 按行读取
with open('test.txt', 'r', encoding='utf-8') as file:
    # 读取一行
    line = file.readline()
    print('第一行：')
    print(line)

    # 读取所有行
    lines = file.readlines()
    print('剩余行：')
    print(lines)

# 遍历文件
with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip()去除行尾的换行符

# 追加内容
with open('test.txt', 'a', encoding='utf-8') as file:
    file.write('Appended line\n')

# 文件指针操作
with open('test.txt', 'r', encoding='utf-8') as file:
    # 移动到文件开头
    file.seek(0)
    # 读取5个字符
    print(file.read(5))
    # 获取当前位置
    print(file.tell())

# 二进制文件操作
with open('binary.bin', 'wb') as file:
    file.write(b'Binary data')

with open('binary.bin', 'rb') as file:
    data = file.read()
    print(data)

# 文件和目录操作
import os

# 检查文件是否存在
print(os.path.exists('test.txt'))

# 获取文件大小
print(os.path.getsize('test.txt'))

# 删除文件
# os.remove('test.txt')

# 创建目录
# os.mkdir('new_directory')

# 获取当前目录
print(os.getcwd())

# 改变当前目录
# os.chdir('new_directory')

# 列出目录内容
print(os.listdir('.'))

# 总结：
# 1. 使用open()函数打开文件
# 2. 文件操作有不同的模式（读、写、追加等）
# 3. 使用with语句自动关闭文件
# 4. 可以按字符、行或全部读取文件
# 5. 可以写入字符串或行列表
# 6. seek()和tell()用于文件指针操作
# 7. 可以操作二进制文件
# 8. os模块提供文件和目录操作功能 