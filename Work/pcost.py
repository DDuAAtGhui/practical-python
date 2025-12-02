# pcost.py
#
# Exercise 1.27
import csv

# manualFilename = "C:/Users/user/Desktop/Workplace/개인/py/practical-python/Work/Data/portfolio.csv"


def portfolio_cost(filename):
    total_price = 0
    with open(f"{filename}", "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(header, row))
            print(record)
            try:
                shares = int(record["shares"])
                price = float(record["price"])
                total_price += shares * price
                
            except ValueError:
                print(f"Row {i} couldn't convert : {row}")
    return total_price


print("Total Cost :::", portfolio_cost("C:/Users/user/Desktop/Workplace/개인/py/practical-python/Work/Data/portfoliodate.csv"))
