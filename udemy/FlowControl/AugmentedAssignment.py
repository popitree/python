number = "9.223.373.036.854.775.807"
cleanedNum = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNum = cleanedNum + number[i]
        # this is augmented assignment combination of binary and assignment
        # this is more efficient in Python unlike in Java and C
        # here variable is evaluated once but above twice in case of Python
        # Python creates a new variable in memory to store the concatenated string
        # and destroy original version in above case
        cleanedNum += number[i]

newNum = int(cleanedNum)
print("the Number is {}.".format(newNum))

x = 25
x **= 2
print(x)


# + and * work with string

greeting = "hello "
greeting *= 2
print(greeting)
