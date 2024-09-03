expenses=[12000,13000,11000,14000,15000,21000,22000,13000]
total_expense=0

#find count of objects in expenses
expense_count=len(expenses)
print(expense_count)


###print all expenses
for i in range(0,len(expenses)):
    print(expenses[i])


###print expenses>15000
for i in range(0,len(expenses)):

    if expenses[i]>15000:

        print(expenses[i])



###print total expenses
    total_expense=total_expense+expenses[i]

print(f"total expense={total_expense}")


###average expense

average_expense=total_expense/len(expenses)
print(f"average expense ={average_expense}")
