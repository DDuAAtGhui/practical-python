# pcost.py
#
# Exercise 1.27
import os

# os.chdir("c:/Users/MAINUSER/Desktop/교육/Python/practical-python/Work")

def portfolio_cost(dir,filename):
    total_price = 0
    with open(f"{dir+filename}", "rt") as f:
        header = next(f)
        for line in f:
            row = line.split(",")
            sum_price = int(row[1]) * float(row[2])
            total_price += sum_price
    return total_price

print(f"Total cost {portfolio_cost("C:/Users/user/Desktop/Workplace/개인/py/practical-python/Work/Data/",
                                   'portfolio.csv')}")

