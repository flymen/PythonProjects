# 作业：游戏剪刀石头布
import random

a = int(input("请输入：剪刀（0）、石头（1）、布（2）："))
while a not in [0, 1, 2]:
    a = int(input(f"你的输入为{a},请重新输入："))
b = random.randint(0, 2)
if a == 0:
    print("你的输入为：剪刀（0）")
    print(f"随机生成数字为：{b}")
    if b == 0:
        print("平手！")
    elif b == 1:
        print("哈哈，你输了！")
    elif b == 2:
        print("哈哈，你赢了！")
elif a == 1:
    print("你的输入为：石头（1）")
    print(f"随机生成数字为：{b}")
    if b == 0:
        print("哈哈，你赢了！")
    elif b == 1:
        print("平手！")
    elif b == 2:
        print("哈哈，你输了！")
elif a == 2:
    print("你的输入为：布（2）")
    print(f"随机生成数字为：{b}")
    if b == 0:
        print("哈哈，你输了！")
    elif b == 1:
        print("哈哈，你赢了！")
    elif b == 2:
        print("平手！")
