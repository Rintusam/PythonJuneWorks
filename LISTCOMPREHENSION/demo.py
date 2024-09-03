# lsst=[10,2,3,5,6]

#squares=[return  iteration  condition]

# squares=[n**2 for n in lsst]
# print(squares)

# cubes=[n**3 for n in lsst]
# print(cubes)

# odd_num=[n for n in lsst if n%2!=0 ]
# print(odd_num)

# even_num=[n for n in lsst if n%2==0]
# print(even_num)


words=["fly","flyin","flyout","out","in","flyoff"]

fly_words=[ w for w in words if w.startswith("fly") ]
print(fly_words)