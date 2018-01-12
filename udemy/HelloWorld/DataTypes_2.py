#String is of type SEQUENCE

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

print(parrot[-1]) #0=N, -1 = e

#slice
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])

print(parrot[-4:2])
print(parrot[-4:-8])
#both wont print anything cause cannot go from end to front in reverse order

print(parrot[-4:-2])

#Slicing by skipping characters
print(parrot[0:6:2]) #0 to 6-1 in step of 2 char at 0,2,4
print(parrot[0:6:3]) #0,3 char Nw

numbers = "9,223,123,456,032,889,5567"
print(numbers[1::4]) #from 1st char till end with jump of 4
#output = ,,,,,,7

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9, 1"
print(numbers[0::3])

#concat without +
a = "hello" " " "World" "!"
print(a)

#multiple String
print("a"*5)
#below error due to operator precedence
#print("x"*5+4)

#to check if one string is a substring of other
print("day" in "friday")
print("day1" in "friday")