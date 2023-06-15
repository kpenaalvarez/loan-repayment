# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:41:13 2023

@author: kpenaalvarez
"""
def calculate_monthly_repayment(PV, r, n):
    # Convert APR to monthly interest rate
    monthly_interest_rate = r / (12 * 100)
    
    # Compute the denominator part of the formula
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    
    # Compute the monthly repayment amount
    Pmt = monthly_interest_rate * PV / denominator
    
    return Pmt

# Example usage with PV = 12000, r = 7.45 (APR), n = 48 months
PV = 12000
r = 7.45
n = 48

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly repayment amount: $", round(monthly_repayment, 2))

