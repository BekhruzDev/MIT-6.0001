# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:04:26 2023

@author: Bekhruz Abdullakhujaev
Pset1b
"""
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0.0
months_counter = 0
down_payment = total_cost * portion_down_payment

while(down_payment>current_savings):
    if(months_counter != 0 and months_counter % 6 == 0 ):
        annual_salary += semi_annual_raise * annual_salary
    current_savings += (current_savings * 0.04 / 12) + portion_saved * annual_salary/12
    months_counter += 1

print("Number of months", months_counter)


