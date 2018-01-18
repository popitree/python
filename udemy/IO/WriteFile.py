cities = ["Denver2", "Kolkata1", "Chennai", "Banaglore", "Delhi", "Mumbai"]
with open("cities.txt", mode="w") as city_file:
    for city in cities:
        print(city, file=city_file)
# mode w will overwrite if file exists
# print has flush argument
# By default it is False, so not gets flushed automatically
# flush: external devices are slower than memory
# so data is written into a buffer and buffer contents
# are transferred to the external devices in background
# so program will work without waiting for write to cmplete
# so when the process says finished that time it still
# might be writing something in background
# if external device is screen perhaps you want to write immediately
# otherwise flickering for example
# closing file causes the buffer to be flushed automatically
# if want data to be available as soon as it is available
# flush = True (introduced in Python 3)
# now a days generally not required to use


# We can write to a file but not necessarily read in same format
# for example write a tuple in a file
# but when reading it is string
# so Python has a eval function
# that will evaluate any expression

indra = "Indranil", 98765, (
    (1, "CSCPPR"),
    (2, "WSAPI")
)

with open("indra.txt", "w") as indra_file:
    print(indra, file=indra_file)


with open("indra.txt", "r") as indra_file:
    data = indra_file.readline()

# eval is not a good idea. because contents can be changed
# and for external data it can have instructions
# that program will execute (vulnerable)
indraData = eval(data)

name, empId, projects = indraData
print(projects[0])

