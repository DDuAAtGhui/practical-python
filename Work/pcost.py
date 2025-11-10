# pcost.py
#
# Exercise 1.27
import csv

# manualFilename = "C:/Users/user/Desktop/Workplace/개인/py/practical-python/Work/Data/portfolio.csv"


def portfolio_cost(filename):
    total_price = 0
    with open(f"{filename}", "rt") as f:
        rows = csv.reader(f)

        for row in rows:
            sum_price = int(row[1]) * float(row[2])
            total_price += sum_price
    return total_price


print("Total Cost :::", portfolio_cost(""))
