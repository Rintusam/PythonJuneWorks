arr=[0,1,3,4,5]

n=len(arr)

sum_of_n=n*(n+1)/2

current_sum=sum(arr)

missing_number=sum_of_n-current_sum

print(missing_number)