__author__ = 'dev'
print("Hello World!")
print('Hello World!')
print(7*6)
print('5\n')
print("Python's string")
print()
print("Python\"s string")
#Concat
print("hello"+"world")
name = "Indra"
greeting = "Hello"
print(greeting + ' ' +name)
print("Line\nNextLine")
print("Tabbed 1\t2\t3\t4\t5")

anotherSplitString = """\n\n this string
is splitted over 
several lines

"""

print(anotherSplitString)

print('''Triple quote no backslash worries
 'ha ha ha "hello'ss"  '
  ''')

print(""" Triple quote no backslash worries
 'ha ha ha "hello'ss"  ' ""\"
  """)

age = 31
#Error:
# print(age + " helleo")


print(age.__str__() + " helleo")

print("The End")