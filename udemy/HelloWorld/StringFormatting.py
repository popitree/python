__author__ = 'indra'
age = 24
print("my age is : "+str(age)+" years")
print("my age is : "+age.__str__()+" years")

#replacement fields no need to do + + etc
print("my age is : {0} years".format(age))
print("my age is : {0}, {1} years".format(age,56))
#my age is : 24, 56 years
print("my age is : {0}, {0} years".format(age))
#my age is : 24, 24 years

print("name : {0} and age : {1}".format("rahul",56))

print("""name : {0} 
age : {1}""".format("rahul",56))

#deprecated in Python3 old format
print("My Age is %d years" %age)
print("My Age is %d %s,%d %s" %(age, "years", 6, "months"))

#%4d left padded
for i in range(1, 12):
    print("No. %-2d squared is %4d and cubed is %4d " %(i, i ** 2, i**3))

#formatting for fractaions
print("pi is approx %12f" %(22/7))
#pi is approx     3.142857  #by default 6 decimal

print("pi is approx %12.12f" %(22/7))
#pi is approx 3.142857142857


for i in range(1, 12):
    print("No. {0:<2} squared is {1:4} and cubed is {2:4} " .format(i, i ** 2, i**3))

print("pi is approx {0:12.12}".format(22/7))


print("2nd: {1} and first : {0}".format(1,2))

print("2nd: {} and first : {:5} .".format(1,2))