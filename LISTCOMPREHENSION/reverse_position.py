arr=[10,11,12,13,14,15,16,17]
    # 0  1  2  3  4  5  6  7 

#reverse odd positions
#odd_pos_num=[11,13,15,17]

left=1

length=len(arr)-1

if length%2!=0 :
    right=length

else:
    length-1

while(left<right):

    (arr[left],arr[right])=(arr[right],arr[left])

    left=left+2

    right=right-2

print(arr)
