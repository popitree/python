# Append multiplication table to test.txt

with open("test.txt", mode="at") as table:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{:2} times {} is {:4}".format(j, i, i*j), file=table)
        print("="*40, file=table)
