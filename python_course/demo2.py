# -*- coding: utf-8 -*-
# @Time : 2024/7/22 上午11:57
# @Author : Jun Bao
# @File : demo2.py
# @Software : PyCharm


# 打印九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()
"""


# 将8个老师随机分配到3个办公室
"""
import random

office = [[], [], []]
teachers = ["teacher1","teacher2","teacher3","teacher4","teacher5","teacher6","teacher7","teacher8"]
for teacher in teachers:
    officeNum = random.randint(0, 2)
    office[officeNum].append(teacher)
print(office)
"""

"""
# 作业：根据商品列表添加商品至购物车，直到客户输入q时退出，并打印购买的商品表列
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("------  商品列表  ------")
i = 0
for product in products:
    print(f"{i}\t{product[0]}\t{product[1]}")
    i += 1

cart = []
item = ""
while True:
    item = input("请输入你想购买的商品编号:")
    if item.isdigit() and int(item) <= len(products):
        cart.append(products[int(item)])
        print(f"商品{item}已添加至购物车。")
    elif item.isalpha() and item == "q":
        break
    else:
        print("输入无效，请重新输入！")
        continue

j = 0
sum_price = 0
print("------  购买商品列表  ------")
for product_buy in cart:
    print(f"{product_buy[0]}\t{product_buy[1]}")
    j += 1
    sum_price += product_buy[1]
print(f"您共购买{j}件商品，总价为{sum_price}元。")
"""
