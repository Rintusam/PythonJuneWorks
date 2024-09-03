# monthly emi
# total payment
# total interest payable

# read loan maount, tenure,interest rate from the user

Loan_amount=int(input("enter the Loan amount = "))

tenure=int(input("tenure = "))

interest_rate=int(input("interest rate = "))

tenure_in_months=tenure*12

monthly_interest_rate=interest_rate/12/100
# EMI=(p*r*(1+r)**n)/((1+r)**n-1)

monthly_EMI=(Loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**tenure_in_months)/(((1+monthly_interest_rate)**tenure_in_months-1))

print(f"montly emi = {monthly_EMI}")

total_payment=monthly_EMI*tenure_in_months

total_interest_payable=total_payment-Loan_amount

print(f"total payment={total_payment}")

print(f"total interest payable={total_interest_payable}")




           
