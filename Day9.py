from itertools import permutations

with open("Day9input.txt") as f:
    data = f.readlines()

places = []
dist = dict()

for line in data:
    word = line.split()
    if not word[0] in places:
        places.append(word[0])
    if not word[2] in places:
        places.append(word[2])
    dist[word[0]+word[2]] = int(word[4])
    dist[word[2]+word[0]] = int(word[4])

perms = list(permutations(places))


def length(pl):
    d = 0
    for i in range(len(pl)-1):
        d += dist[pl[i]+pl[i+1]]
    return d


shortest = length(perms[0])
longest = 0
for p in perms:
    current = length(p)
    if current < shortest:
        shortest = current
    if current > longest:
        longest = current

print(shortest)
print(longest)
