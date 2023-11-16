# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:30:43 2023

@author: Bekhruz Abdullakhujaev
"""

annual_salary = int(input("Enter your annual salary: "))
semi_annual_raise = 0.07
total_cost = 1_000_000
portion_down_payment = 0.25
current_savings = 0.0
months = 36
down_payment = total_cost * portion_down_payment

low = 0
high = 10000
steps = 0

while(abs(high - low) > 1):  # BE CAREFULL WHEN COMPARING FLOATS
    current_savings = 0
    annual_salary_copy = annual_salary
    mid = (low + high) / 2
    steps += 1
    for month in range(36):
        if(month % 6 == 0 and month != 0):
            annual_salary_copy += annual_salary_copy * 0.07
        current_savings += (current_savings * 0.04 / 12) + \
            (mid / 10_000) * (annual_salary_copy/12)

    offset = current_savings - down_payment
    if(offset < -100):
        low = mid
    elif (offset > 100):
        high = mid
    else:  # additional break
        break

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", mid / 10_000)
    print("Steps in bisection search", steps)
