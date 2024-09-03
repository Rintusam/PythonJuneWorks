# create a function nth_digit_max with two parameter num1,num2
#nth_digit_max(123,480) =>123
#nth_digit_max(546,127) =>127


# def nth_digit_max(num1,num2):

#     num1_last_digit=num1%10

#     num2_last_digit=num2%10

#     if num1_last_digit>num2_last_digit:

#         return num1
    
#     else:

#         return num2
    
# print(nth_digit_max(123,480))


                        # OR



def nth_digit_max(num1,num2):

    return num1 if num1%10>num2%10 else num2

print(nth_digit_max(123,480))
