#
#     ---------------▶5 Forest
#     │                   ▲
#     │                   │
#     │                   │
#     │                   │
#     ▼                  ▼
#   2 Hill◀----------- 1 Road◀---------▶3 Building
#     ▲                  ▲
#     │                   │
#     │                   │
#     │                   │
#     │                   ▼
#       ------------- 4 Valley


locations = {0: "You are in front of computer",
             1: "In Road",
             2: "On top of hill",
             3: "Inside building",
             4: "In valley beside a stream",
             5: "In dark forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"S": 1, "W": 2, "Q": 0}]

loc = 1
while True:
    availabelExits = ", ".join(exits[loc].keys())


    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits:["+availabelExits+"]\nYour Choice:").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("can not go into the direction")




