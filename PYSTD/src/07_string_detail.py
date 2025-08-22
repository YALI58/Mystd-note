# 07_string_detail.py
# 2025/1/16   16:50

# 字符串注意事项

# 使用引号''或""包括起来,创建字符串
print("'hello'")

# 使用+号链接字符串
print("ada" + "adafa")  # adaadafa

# python中不支持单字符类型,单字符在python中也是作为一个字符串使用


# 用三个单引号'''内容''',或三个双引号都可以使字符串内容保持原样输出,比如输出一段代码
content = '''
if 0:
    print("hh")  # 不输出
if -1:
    print("xx")  # xx
    '''
print(content)

# 字符串前面加'r',可以使整个字符串不被转义

str = r"jtck\ntia\tk"
str1 = "jtck\ntia\tk"
print(str)  # jtck\ntia\tk

print(str1)  # jtck
# tia	    k

# 字符串驻留机制
str1 = "helllo"
str2 = "helllo"
str3 = "helllo"

print("str1: ", id(str1))  # str1:  1515608789360
print("str2: ", id(str2))  # str2:  1515608789360
print("str3: ", id(str3))  # str3:  1515608789360 