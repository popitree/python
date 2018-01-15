# Ordered set of Data
# Immutable
# parenthesis is not mandatory
a = 12, 13
b = (12, 13)
print(a == b)

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