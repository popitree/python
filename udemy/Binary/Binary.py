for i in range(17):
    print("{0:>2} in binary is {0:>05b}".format(i))

print("="*20)

for i in range(17):
    print("{0:>2} in hex is {0:>3x}".format(i))

print("="*20)

for i in range(17):
    print("{0:>2} in octal is {0:>3o}".format(i))

# XOR
# if repeated gives the original number back
# 55 -      1 1 0 1 1 1
# xor 11    0 0 1 0 1 1
# --------------------------
# 60        1 1 1 1 0 0
# xor 11    0 0 1 0 1 1
# --------------------------
# got 55    1 1 0 1 1 0
print("="*20)

print(0x20)
print(0b1100011)
print(0o40)
