myList = ["A", "B", "C", "D"]
newString = ''
for c in myList:
    newString += c + ", "

print(newString)

# Strings are immutable hence not efficient while concatenating in a loop
# Join to rescue
# trailing comma issue also resolved
newString1 = ", ".join(myList)
print(newString1)

# Any sequence can be used for join
print("-".join("1234"))

print(" tick ".join(["one", "two", "three", "four"]))



