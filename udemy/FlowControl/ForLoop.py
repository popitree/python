for i in range (1,3):
    print("i is now {:4}".format(i))

number  = "9,123,456,035,654"
for i in range (0, len(number)):
    print(str(i) + ' ' +number[i])

for i in range (0, len(number)):
    if(number[i] in "0123456789"):
        print(number[i] ,end=' ')

cleanedNum = ''
for i in range (0, len(number)):
    if(number[i] in "0123456789"):
        cleanedNum = cleanedNum + number[i]  #concatenation

print("\n\nNumber is: {}".format(int(cleanedNum)))
cleanedNum = ''
#Python Iterates over sequence of anything, not like i increment by something and do as in java
for char in number:
    if char in "0123456789":
        cleanedNum = cleanedNum + char
print("\n\nNumber is: {}".format(int(cleanedNum)))

for state in ["CO", "NY", "CA"]:
    print("travelling in {}".format(state))

for i in range (0,10,3):
    print("i is now {:4}".format(i))

#Multiplication table
for i in range(1,11):
    for j in range(1,11):
        print("{:2} x {:2} = {:3}".format(j,i,i*j), end='\t')
    print()