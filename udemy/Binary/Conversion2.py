# lets say highest is 2 ** 16 - 1 = 65535
# generate list of powers
powers = []
for i in range(15, -1, -1):
    powers.append(2 ** i)

decimal = 65535
x = decimal
isPrintStart = False
for power in powers:
    bit = x // power

    if bit != 0 or power == 1:
        isPrintStart = True
    if isPrintStart:
        print(bit, end="")
    x %= power
