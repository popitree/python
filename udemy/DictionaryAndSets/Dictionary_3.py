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

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"S": 1, "W": 2, "Q": 0}}

exitWords = {"NORTH": "N",
             "SOUTH": "S",
             "EAST": "E",
             "WEST": "W",
             "QUIT": "Q"}

loc = 1
while True:
    availabelExits = ", ".join(exits[loc].keys())


    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits:["+availabelExits+"]\nYour Choice:").upper()
    if len(direction) > 1:
#       direction = exitWords.get(direction)
        words = direction.split()
        for word in words:
            if word in exitWords:
                direction = exitWords[word]
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("can not go into the direction")




