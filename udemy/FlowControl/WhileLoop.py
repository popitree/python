i = 1
while i < 5:
    print(i)
    i += 1

available_exists = ["east", "north_east", "south"]
chosen_exit = ''
while chosen_exit not in available_exists:
    chosen_exit = input("Enter exit:")
    if chosen_exit == 'quit':
        print("game Over")
        break
print("Whoa out of loop")

while chosen_exit not in available_exists:
    chosen_exit = input("Enter exit:")
    if chosen_exit == 'quit':
        print("game Over")
        break
else:   #else for while break
    print("Whoa out of loop")
