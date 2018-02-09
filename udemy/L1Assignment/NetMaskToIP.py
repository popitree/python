subList = list()
for i in range(0, 8):
    subList.insert(i, 2 ** i)

while 1:
    netMask = input("Enter Netmask:")
    if netMask == "quit":
        break
    try:
        netMask = int(netMask)
        if netMask < 0 or netMask > 32:
            raise ValueError
    except ValueError:
        print("Enter Correct Value")
        continue

    myList = list()
    quotient = netMask // 8
    modulo = netMask % 8

    sum = 0
    for i in range(8 - modulo, 8):
        sum = sum + subList[i]

    for i in range(0, 4):
        if i == quotient and modulo > 0:
            myList.insert(i, sum)
        elif i < quotient:
            myList.insert(i, 255)
        else:
            myList.insert(i, 0)

    print("NetMask : "+".".join(str(x) for x in myList))
    print("Wildcard : "+".".join(str(255-x) for x in myList))
