# Author: StevenChaoo
# -*- coding:UTF-8 -*-


def f1():
    print("******* This tool is used to calculate f1 score *******")
    print("\n")
    pre = input("Please enter the precision value: ")
    rec = input("Please enter the recall value: ")
    print("\n")
    temp_1 = float(pre)+float(rec)
    temp_2 = float(pre)*float(rec)
    f1_value = 2*temp_2/temp_1
    f1_value = round(f1_value, 2)
    print("******* The f1 score value is {} *******".format(f1_value))
    print("\n")
