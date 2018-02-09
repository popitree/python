from Tools.demo.sortvisu import SortDemo

mylist = list(range(4))

seclist = mylist
print(seclist)

mylist.append(4)

# Here seclist points to main list
print(seclist)

# this slicing returns new list which is assigned to seclist variable
seclist = mylist[:]

mylist.append(5)

print(seclist)


# --------------------------------------------------------
def f(n):
    for x in range(n):
        yield x ** 3


for x in f(6):
    print(x)
# --------------------------------------------------------
# data = input("Enter a text:")
data = "EE"
eCount = data.count("e")
if eCount == 2:
    print(True)
else:
    print(False)
# --------------------------------------------------------
counter = 1


def dolots(count):
    global counter
    for i in (1, 2, 3):
        counter = count + i


print(dolots(4))
print(counter)
# --------------------------------------------------------
list1 = [10, 15, 13, 28, 11]
list2 = [123, 10, 54]
list3 = [98, 0, 4]

sorted1 = sorted(list1)
sorted2 = sorted(list2)
sorted3 = sorted(list3)

minList = sorted1[:2] + sorted2[:2] + sorted3[:2]
maxList = sorted1[-2:] + sorted2[-2:] + sorted3[-2:]

import functools

print("maxList:{}".format(maxList))
print("maxList avg: {}".format((functools.reduce(lambda x, y: x + y, maxList)) / len(maxList)))

print("minList:{}".format(minList))
print("minList avg: {}".format((functools.reduce(lambda x, y: x + y, minList)) / len(minList)))
# --------------------------------------------------------
