# r = reda mode
jabberwocky = open("sample.txt", "r", encoding="UTF-8")

for line in jabberwocky:
    if "jabberwock" in line.lower():
        # file line already has newline character
        print(line, end='')

jabberwocky.close()

print("="*40)
# Pythonic way
# If object supports with statement then it will take care of
# closing etc tasks, no need to do error handling
# with will trap the excpetion and close the file before
# error terminates the program

with open("sample.txt", "r", encoding="UTF-8") as jabber:
    for line in jabber:
        if "jabberwock" in line.lower():
            print(line, end='')
print("="*40)

# generally in other languages
# this is preferrable as read line by line, not fully as in next cases
with open("sample.txt", "r", encoding="UTF-8") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()
print("\n")
print("="*40)


# readlines gives array of lines
with open("sample.txt", "r", encoding="UTF-8") as jabber:
    lines = jabber.readlines()
    # this is array of lines
    print(lines, end='')
print("\n")
print("="*40)
# can do it in reverse
for line in lines[::-1]:
    print(line, end='')
print("="*40)
print("="*40)


# This will completely reverse: read function
# read is more useful for binary files
# gives one string
with open("sample.txt", "r", encoding="UTF-8") as jabber:
    lines = jabber.read()
    # Array of characters
# can do it in reverse
for line in lines[::-1]:
    print(line, end='')