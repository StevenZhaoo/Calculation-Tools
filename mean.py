# Author: StevenChaoo
# -*- coding:UTF-8 -*-


def mean():
    print("******* This tool is used to calculate mean value *******")
    print("\n")
    stock = []
    amount = 0
    while True:
        num = input("Please enter the number (cease with 'quit'): ")
        if num != "quit":
            stock.append(float(num))
            amount += float(num)
        else:
            break
    print("\n")
    length = len(stock)
    mean_value = amount/length
    print(f"******* The mean value is {round(mean_value, 2)} *******")
    print("\n")
