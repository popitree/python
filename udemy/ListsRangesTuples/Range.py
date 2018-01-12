# Range in Python3 is a data type
# in 2 it was a function

print(range(10))
# range(0, 10) means range starts at 0, till 10 but not 10

for i in range(10, 14, 2):
    print(i)

# to create list
my_list = list(range(10))
print(my_list)

print(list(range(1, 10, 2)))
print(list(range(0, 10, 2)))

# python ranges are very memory efficient
# range(0,10) and range(0,11111) will take same space
# In Python2 range values were calculated and returned as sequence
# In python2 xrange became range in python3 and no xreange in 3

# range can not perform all operations that can be performed on sequence.
# range is sequence with defined pattern+
# no multiplication or concatenation of range

# INDEX
my_str = "abcdefghijklmnopqrstuvwxyz"
print(my_str.index('e'))
print(my_str[4])

# Throw error if not in sequence
print(range(1, 1000000, 2).index(989))

# Use in operator
print(2 in range(10))

# sub range
oldRange = range(100)
newRange = oldRange[3:35:5]
print(list(newRange))

print(range(1, 45, 3) == oldRange[1:45:3])
# True
print(range(0, 5, 2) == range(0, 6, 2))
# True cause values in range are same


r = range(0, 100)
# r = 0,1,...99
# ranges below are 99 97 95 ... 1
print(r[::-2] == range(99, 0, -2))

# Wont print anything, if negative then the start and end value
# also should be in that order
# this will work for slice (negative slice)
for i in range(0, 100, -1):
    print(i)

# use of negative slice to reverse a string
print("emoclew"[::-1])

o = range(0, 100, 4)
print(o)
p = o[::5] # range 0, 100, 20
print(p)
for i in p:
    print(i)



o
