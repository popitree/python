# Ordered set of Data
# Immutable
# parenthesis is not mandatory
a = 12, 13
b = (12, 13)
print(a == b)

welcome = "Welcome", "Alice", 10
bad = "bad", "jane", 20

print(bad)
print(bad[2])

# Error as immutable
# bad[2] = 20

# To change, so assigning new object to variable
# also check right hand is evaluated first, hence no error
bad = bad[0], bad[1], 35
print(bad)

# if list we can update
even = [2, 4, 6]
even[2] = 8
print(even)

# It is not like the variable is immutable.
# But the object the variable is referring to

# Lists are intended to contain similar types Homogeneous, though not enforced
# But tuples are to contain different types
# Dictionary key should be immutable object. Where tuple is useful.
# Then as it is immutable and you cannot change so useful to remove bugs in programs

# Unpacking the tuple (into variables)
movie = ("Tiger Zinda Hai", ["Salman", "Katrina"], 2017)
movieName, artists, year = movie
print("""
Movie Details: 
Name:{}
Artists:{}
Year:{}
""".format(movieName, artists, year))
