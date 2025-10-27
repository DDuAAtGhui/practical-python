# pcost.py
#
# Exercise 1.27
import os

os.chdir("c:/Users/MAINUSER/Desktop/교육/Python/practical-python/Work")

pf = "Data/portfolio.csv"

total_price = 0

with open(pf, "rt") as f:
    print(f.read())

with open(pf, "rt") as f:
    header = next(f)
    for line in f:
        row = line.split(",")
        sum_price = int(row[1]) * float(row[2])
        total_price += sum_price

print(f"Total cose {total_price}")
