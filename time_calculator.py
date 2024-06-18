import datetime


def countDays():
    d1 = input(f"Day 1 is: (yyyymmdd) ")
    d2 = input(f"Day 2 is: (yyyymmdd) ")
    date1 = datetime.datetime(int(d1[:4]), int(d1[4:6]), int(d1[6:]))
    date2 = datetime.datetime(int(d2[:4]), int(d2[4:6]), int(d2[6:]))
    interval = date2-date1
    print(f"{interval.days + 1} Days\n\n")
