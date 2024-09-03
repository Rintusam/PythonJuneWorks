arr=[
    [10,20],
    [20,35],
    [41,50]
]

#sum
# numbers=[]
# for lst in arr:  #[10,20]

#     for num in lst:
#         numbers.append(num)

# print(sum(numbers))

                #or

# numbers=[num for lst in arr for num in lst]
# print(sum(numbers))

evens=[num for lst in arr for num in lst if num%2==0]
print(evens)

num_gt_15=[num for lst in arr for num in lst if num>15]
print(num_gt_15)