# read start_limit and end_limit from user and print all odd numbers from start_limit to end_limit

start_limit=int(input(" start limit = "))

end_limit=int(input("end limit = "))


for i in range(start_limit,end_limit+1):
    
    if i%2!=0:

        print(i)