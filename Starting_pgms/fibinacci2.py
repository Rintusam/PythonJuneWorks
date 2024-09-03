num=int(input("enter number = "))

previous=0

current=1

Isfibo=False

if num in (0,1):
        
    Isfibo=True

    next=previous+current

    while(next<=num):

        next=previous+current

        previous=current

        current=next

        if next==num:

            Isfibo=True

            break

print(Isfibo)

