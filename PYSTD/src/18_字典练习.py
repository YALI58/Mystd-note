# 18_字典练习.py
# 2025/1/25   21:23

# 练习1：创建和访问字典
# 创建一个学生信息字典
student = {
    'name': '张三',
    'age': 18,
    'scores': {
        'Chinese': 85,
        'Math': 92,
        'English': 88
    }
}

# 访问字典中的值
print(f"学生姓名：{student['name']}")
print(f"学生年龄：{student['age']}")
print(f"数学成绩：{student['scores']['Math']}")

# 练习2：字典的增删改查
# 创建空字典
contacts = {}

# 添加元素
contacts['Tom'] = '123456'
contacts['Jerry'] = '789012'
print("\n添加后的通讯录：", contacts)

# 修改元素
contacts['Tom'] = '111111'
print("修改后的通讯录：", contacts)

# 删除元素
del contacts['Jerry']
print("删除后的通讯录：", contacts)

# 练习3：字典方法的使用
# 创建商品价格字典
prices = {
    'apple': 5,
    'banana': 3,
    'orange': 4,
    'grape': 8
}

# 获取所有商品名
products = prices.keys()
print("\n所有商品：", list(products))

# 获取所有价格
all_prices = prices.values()
print("所有价格：", list(all_prices))

# 获取商品和价格的键值对
items = prices.items()
print("商品价格对：", list(items))

# 练习4：字典推导式
# 创建一个平方数字典
squares = {x: x**2 for x in range(1, 6)}
print("\n数字平方字典：", squares)

# 练习5：字典的遍历
print("\n遍历商品价格：")
for product, price in prices.items():
    print(f"{product}的价格是：{price}元") 