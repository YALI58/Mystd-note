# 06_递归.py
# 2025/1/21   14:54


# 斐波那契
def fbn(a):
    '''
    :param a:
    :return 每个斐波那契数:
    '''
    if a == 1 or a == 2:
        return 1
    else:
        return fbn(a - 1) + fbn(a - 2)


print(fbn(6))


# 猴子吃桃
def monkey_fruit(day):
    """
    :param day:
    :return:
    """
    if day == 10:
        return 1
    else:
        return 2 * (monkey_fruit(day + 1) + 1)


print(monkey_fruit(1))


# 汉诺塔

def hanoi_power(num, a, b, c):
    if num == 1:
        print(f"第1个盘从{a}->{c}")
    else:
        #从a到b,借用c
        hanoi_power(num - 1, a, c, b)
        # 将最下面的移动到c
        print(f"第{num}个盘从{a}->{c}")
        #从b到c借用a
        hanoi_power(num - 1, b, a, c)

hanoi_power(3,"A","B","C") 