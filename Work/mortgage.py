# mortgage.py
#
# Exercise 1.7
# mortgage.py


def totalPaid(principal, rate, payment, exPayStartMon=0, exPayEndMon=0, exPay=0):
    total_paid = 0
    elap_month = 0
    while principal > 0:
        elap_month += 1

        principal = principal * (1 + rate / 12) - payment
        total_paid += payment

        if elap_month >= exPayStartMon and elap_month <= exPayEndMon:
            principal -= exPay
            total_paid += exPay

        print(f"{elap_month} {total_paid} {principal}")

        if principal < payment:
            total_paid += principal
            principal = 0
            elap_month += 1
            print(f"{elap_month} {total_paid} {principal}")
            break

    print(f"Elapsed Month : {elap_month}, TotalPaid : {total_paid}")


totalPaid(500000.0, 0.05, 2684.11, 61, 108, 1000)
