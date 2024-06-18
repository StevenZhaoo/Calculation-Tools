# Author: StevenChaoo
# -*- coding:UTF-8 -*-


from f1 import f1
from mean import mean
from time_calculator import countDays

while True:
    select_num = input(
        "PLEASE SELECT THE CALCULATION TOOL\n01: F1 Score Value\n02: Mean Value\n03: Count Days\n\nSelection: ")
    print("\n")
    if select_num == "01":
        f1()
    elif select_num == "02":
        mean()
    elif select_num == "03":
        countDays()
