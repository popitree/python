#INT
#python3 does not have limit on IN (limited by available memory
import sys


print(sys.maxsize)
print(sys.maxsize+1)
print(pow(2,32))

a = 12
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a / b)  #as float
print(a // b) #to return as integer
print(a % b)

for i in range(1,4):
    print(i)

for i in range(1,a//b):  #a/b will give error as a/b gives float
    print(i)

#When same operator precedence then evaluate from left to right
print(a/b*3)
print(a*b/4)
#Floating point number has 52 digits of precision


