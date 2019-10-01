with open("Day16input.txt") as f:
    data = f.readlines()

detected = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

props = []
for line in data:
    words = line.replace(":", " ").replace(",", " ").split()
    props.append([[words[2], int(words[3])], [words[4], int(words[5])], [words[6], int(words[7])]])

for i, things in enumerate(props):
    ok = 0
    for item in range(3):
        if detected[things[item][0]] == things[item][1]:
            ok += 1
    if ok == 3:
        print(i+1)

# part 2

for i, things in enumerate(props):
    ok = 0
    for item in range(3):
        if things[item][0] == "cats" or things[item][0] == "trees":
            if detected[things[item][0]] < things[item][1]:
                ok += 1
        elif things[item][0] == "pomeranians" or things[item][0] == "goldfish":
            if detected[things[item][0]] > things[item][1]:
                ok += 1
        else:
            if detected[things[item][0]] == things[item][1]:
                ok += 1

    if ok == 3:
        print(i+1)
