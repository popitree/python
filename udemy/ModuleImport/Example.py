# Core build in modules are imported implicitly
# there is nothing as private in Python
# _ is to indicate intention: Do not change
print(dir())

# result
# ['__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__']

# for m in dir(__builtins__):
#     print(m)


import shelve
# help(shelve)

for obj in dir(shelve.Shelf):
     if obj[0] != "_":
         print(obj)


