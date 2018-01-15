decimal = 65536

x = decimal
binary = ""
while x != 0:
    a = x % 2
    x = x//2

    binary += str(a)

print("{} in binary is {}".format(decimal, binary[::-1]))

print("="*9)

x = decimal
octal = ""
while x != 0:
    a = x % 8
    x = x//8

    octal += str(a)

print("{} in octal is {}".format(decimal, octal[::-1]))