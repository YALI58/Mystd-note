# 04_嵌套分支.py
# 2025/1/19   15:10

score = float(input("成绩:"))

if score>8.0:
    gender = input("性别:")
    if gender=='男':
        print("男子组")
    else:print("女子组")
else:print("淘汰") 