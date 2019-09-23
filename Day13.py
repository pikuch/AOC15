from itertools import permutations

with open("Day13input.txt") as f:
    data = f.readlines()

people = []
moods = dict()

for line in data:
    words = line.replace(".", "").split()
    if not words[0] in people:
        people.append(words[0])
    moods[words[0] + words[-1]] = -int(words[3]) if words[2] == "lose" else int(words[3])

perms = list(permutations(people))
maxMood = -(10**10)

for p in perms:
    currentMood = 0
    for i, name in enumerate(p):
        currentMood += moods[name+p[(i-1+len(p)) % len(p)]]
        currentMood += moods[name+p[(i+1+len(p)) % len(p)]]

    if currentMood > maxMood:
        maxMood = currentMood

print(maxMood)

# part 2

for person in people:
    moods["Me"+person] = 0
    moods[person+"Me"] = 0

people.append("Me")

perms = list(permutations(people))
maxMood = -(10**10)

for p in perms:
    currentMood = 0
    for i, name in enumerate(p):
        currentMood += moods[name+p[(i-1+len(p)) % len(p)]]
        currentMood += moods[name+p[(i+1+len(p)) % len(p)]]

    if currentMood > maxMood:
        maxMood = currentMood

print(maxMood)
