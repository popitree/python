# Sequence - Lists Tuple Range

# lists can contain string which is sequence of characters
# lists can contain list of lists too
# anything including sequence
words = input("Enter sentence:")
print(words.count("a"))

stateList = ["CO", "CA"]
stateList.append("UT")
for state in stateList:
    print("You are travelling to : "+state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(numbers)

# This will print None
# Python behavior: sort method works on object rather than creating/returning a object
# generally if a method works on an object and changes it (mutates it)
# then it generally does not return anything in Python (None is returned)
print(numbers.sort())

numbers.sort()
print(numbers)

# To keep original intact and create new
numbers1 = even + odd
sortedNumbers = sorted(numbers1)
print(sortedNumbers)

# For lists to be equal elements should be in same order
if numbers1 == sortedNumbers:
    print("Lists are same")
else:
    print("Not Sames")

numbers1.sort()
if numbers1 == sortedNumbers:
    print("Lists are same")
else:
    print("Not Sames")


