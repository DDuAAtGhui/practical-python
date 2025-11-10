# report.py
#
# Exercise 2.4

import csv
from pprint import pprint  # Pretty Print 모듈 임포트

filename = (
    "C:/Users/MAINUSER/Desktop/교육/Python/practical-python/Work/Data/portfolio.csv"
)


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
    with open(f"{filename}", "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            print(row)


read_price(filename)
