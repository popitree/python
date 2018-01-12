string = "world"
for char in string:
    print(char)

# actually whats happening behind the scene

# this style will be mainly used when using our own classes
for char in iter(string):
    print(char)

# iterator is taking care
my_iterator = iter(string)
print("----\n"+next(my_iterator), end="\n----\n")
print(my_iterator)
for i in my_iterator:
    print(i)

# if do nex(iter) continuously will get error and need to handle
# for loop does this internally, till it gets the error
# for loop implicitly creates the iterator from the iterable object

nums = [1, 2, 3, 4, 5, 6]
myNumIter = iter(nums)
for i in range(0, len(nums)):
    print(next(myNumIter))
