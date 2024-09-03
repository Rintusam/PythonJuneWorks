#read total amount, tenure,interest rate and print the followig
    # monthly EMi
    # total interest payable
    #total payment

total_amount=int(input("enter amount = "))

tenure=int(input("enter tenure = "))

tenure_months=tenure*12

interest=int(input("enter interest rate = "))

interest_rate=interest/12/100

monthly_emi=total_amount*interest_rate*(((1+interest_rate)**tenure_months)/((1+interest_rate)**tenure_months-1))

print(f"montly emi = {monthly_emi}")