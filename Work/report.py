# report.py
#
# Exercise 2.4

import csv
from pprint import pprint  # Pretty Print 모듈 임포트

pt = "C:/Users/MAINUSER/Desktop/교육/Python/practical-python/Work/Data/portfolio.csv"

price = "C:/Users/MAINUSER/Desktop/교육/Python/practical-python/Work/Data/prices.csv"


# def portfolio_cost(filename):
#     portfolio = []
#     total_cost = 0
#     with open(f"{filename}", "rt") as f:
#         rows = csv.reader(f)
#         header = next(rows)  # 첫 번째 행은 헤더이므로 건너뜀

#         for row in rows:
#             portfolio.append(
#                 {
#                     "name": row[0],
#                     "shares": int(row[1]),
#                     "price": float(row[2]),
#                 }
#             )
#             total_cost += int(row[1]) * float(row[2])
#     return portfolio


def read_price(filename):
    result = {}
    with open(f"{filename}", "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                result[row[0]] = float(row[1])
    # pprint(result)
    return result


def read_portfolio(filename):
    result = []
    with open(f"{filename}", "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        # print(f"header: {header}")
        for row in rows:
            if row:
                result.append((row[0], int(row[1]), float(row[2])))

    # pprint(result)
    return result


def make_report(portfolio, prices):
    report = []
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}")
    print(
        "-" * (len(headers[0]) + 5),
        "-" * (len(headers[1]) + 5),
        "-" * (len(headers[2]) + 5),
        "-" * (len(headers[3]) + 4),
    )
    for name, shares, price in portfolio:
        current_price = prices[name]
        delta_price = current_price - price
        report.append((name, shares, current_price, round(delta_price, 4)))
        print(
            f"{name:>10} {shares:>10} {f'$ {current_price}':>10} {delta_price:>10.4f}"
        )

    return report


# print("========== prices ========= ")
prices = read_price(price)

read_portfolio(pt)

make_report(read_portfolio(pt), prices)
