# It is like java map, unordered
employee = dict(indranil=18100, vikas=15000, mahesh=10100)

employees = {"indranil" : 18100,
            "vikas" :   15000,
            "mahesh" :  10100,
            "vikas" : 14000,
            "special": "xx10"}
# VIKAS key value will override
# Special value is not int

print(employee["vikas"])
print(employees["vikas"])
print(employees["special"])

# Keys can be different objects and they must be immutable
# hence list can not be a dictionary key
# Adding to dictionary
employee["vik"] = "dd100"
# if key does not exist will give error while retrieving
# print(employee["santa"])

# to get around this use get method which return None if key does not exist
print(employee.get("sanat"))
#190458

print(employee)
# deleting
del employee["mahesh"]
print(employee)


# to delete entire dictionary including the variable itself
del employees
# This will give error
# print(employees)


while True:
    key = input("enter employee name:")
    if key == 'quit':
        print("bye...")
        break
    if key in employee:
        print("employee id:{}".format(employee.get(key)))
    else:
        print("We don't have employee:"+key)
# In Python 2, now deprecated
# employee.has_key("")

# if key does not exist, and to give default value
print(employee.get("rubayea", "This employee does not exist"))

# to empty dictionary
employee.clear()
print(employee)

# instead of ordered dictionary, which probably we need when printing the data
# best way to keep it natural - unordered and use a list to get the keys
# then sort that then iterate over it to get the dictionary data

fruits = {"apple": "red", "orange": "orange", "lime": "green", "mango": "yellow"}
fruit_keys = list(fruits.keys())
# fruits.keys() will give keyview on which sort can not be used directly.
# hence converting it to list
fruit_keys.sort()

for fruitName in fruit_keys:
    print(fruitName + "==" + fruits.get(fruitName))
# sorted method can work on keyviews
for fruitName in sorted(fruits.keys()):
    print(fruitName + "==" + fruits[fruitName])

# This is less efficient than using keys to get the same result
for val in fruits.values():
    print(val)

print(fruits.keys())
print(fruits.values())
# Both returns list like objects
# dict_keys and dict_values
# They are called View objects. If underlying dict changes it changes its values
keys = fruits.keys()
print(keys)
fruits["peach"] = "peach"
print(keys)





