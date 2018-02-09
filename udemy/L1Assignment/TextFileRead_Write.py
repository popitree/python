characterCount = list()
wordCount = list()
with open("cities.txt", "r", encoding="UTF-8") as cities:
    for line in cities:
        characterCount.append(len(line))
        wordCount.append(len(line.split(" ")))

with open("citiesCharacterAndWordCount.txt", "w", encoding="UTF-8") as cities:
    for line in range(0, len(characterCount)):
        print("line: {} characters: {} words: {}"
              .format(line+1, characterCount[line], wordCount[line]), file=cities)
