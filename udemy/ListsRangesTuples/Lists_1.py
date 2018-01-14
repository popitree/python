list_1 = []
list_2 = list()
# Both cases will create empty list.
# second one using constructor
print(list_1 == list_2)
# can call constructor with single iterable paramter
# all sequence are iterable including string
list_3 = list("ab cd")
# character list will be produced
print(list_3)


# Both will be sorted as both points to exact same list
even = [2, 4 ,6, 8]
even_1 = even
# Both are same ('is' is for refernce equality)
print(even_1 is even)
even_1.sort(reverse=1)
print(even)
print(even_1)

# if we pass to constructor it will create anoter refernce and 'is' equality will fail
even_2 = list(even)
print(even_2 is even) #False
print(even_2 == even) #True

print(sorted("abcde", reverse=True))


even_x = [2, 4, 6, 8]
odd_x = [1, 3, 5, 7, 9]

print([even, even_1]) #list of lists

for numbers in [even_x, odd_x]:
    print(numbers)

    for number in numbers:
        print(number,end=" ")
    print()