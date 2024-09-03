# p=>loan amount

# r=>interest rate (p.a)=> p.m

# t=>tenure(years)=>months
          
          
Loan_amount=200000  #p

interest_rate=9    #r

Tenure=1  #n

# EMI= p*r*(1+r)**n/(1+r)**n-1

monthly_interest_rate=interest_rate/12/100

tenure_in_months=Tenure*12

monthly_emi=(Loan_amount*monthly_interest_rate*((1+monthly_interest_rate)**tenure_in_months)/(((1+monthly_interest_rate)**tenure_in_months)-1))

print(f"monthly emi = {monthly_emi}")

total_payable_amount=monthly_emi*tenure_in_months

print(f"total amount = {total_payable_amount}")

total_interest_payable= total_payable_amount-Loan_amount

print(f"intrest amount={total_interest_payable}")