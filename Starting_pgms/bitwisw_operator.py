#bitwize operators(&,|,^)

# x     y    x&y     x|y     x^y

# 0     0     0       0       0
# 0     1     0       1       1
# 1     0     0       1       1
# 1     1     1       1       0


# print(0^0)    #xor
# print(0^1)
# print(1^0) 
# print(1^1)

# print(0|0)    #or
# print(0|1)
# print(1|0)
# print(1|1)

# print(0&0)    #and
# print(0&1)
# print(1&0)
# print(1&1)
    

print(2&4)
#0010
#0100
#=====
#0000=>0

print(3|4)
#0011
#0100
#=====
#0111=>7

print(2^4)
#0010
#0100
#=====
#0110=>6
