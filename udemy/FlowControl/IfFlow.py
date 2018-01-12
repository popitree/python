name = input("Your name:")
age = int(input("How old are you {} ?".format(name)))
print(age)

print("False Empty")
if age > 18:
    print("old enough to vote")
    if age >= 60:
        print("Senior Citizen")
    else:
        "Adult"
elif age == 18:
    print("Exact")
else:
    print("Not old enough to vote. Come back in {} years".format(18-age))


print("Age?")
age = int(input())
if age >= 18 and age <23:
    print("young adult1")
if  18 <=  age <23:
    print("young adult2")

if age < 16 or age > 60:
    print("Enjoy life")
else:
    print("Job call")

#In condition any non zero or non empty value will result in false
#False Empty will be the answer
x = ""
if x:
    print("True Non Empty")
else:
    print("False Empty")

print("""
    False: {0}
    None: {1}
    0: {2}
    0.0: {3}
    list []: {4}
    tuple (): {5}
    string '': {6}
    mapping {{}}: {7}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool({})))


print(not False)
if not 1==1:
    print("not 1==1")
else:
    print("1==1")

if "in" in "into":
    print( " in is in into")

if "in" not in "into":
    print( " in is in into")
else:
    print("xxxx")
