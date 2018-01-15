# Assigning multiple valuses
a = b = c = d = 12
print(a, b)

# This looks like a tuple but not
a, b = 12, 13
print(a, b)


print("a is {}".format(a))
print("b is {}".format(b))

# Right side is evaluated first.
# To swap for example
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
