fruits = {"apple": "red", "orange": "orange", "lime": "green", "mango": "yellow"}

for fruit in fruits.items():
    print(fruit)
    print(fruit[0]+"-"+fruit[1])

print(fruits.items())
# can convert that as tuple of tuples
f_tuple = tuple(fruits.items())

for breakfast in f_tuple:
    fruit, color = breakfast
    print(fruit, color)

# can convert tuple to dict
print(dict(f_tuple))

# ----------------------------------

print(",".join(fruits.keys()))
