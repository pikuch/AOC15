with open("Day14input.txt") as f:
    data = f.readlines()


class Reindeer:
    def __init__(self, name, sp):
        self.name = name
        self.pointer = 0
        self.speeds = sp
        self.dist = 0
        self.points = 0

    def go(self):
        self.dist += self.speeds[self.pointer]
        self.pointer += 1
        if self.pointer >= len(self.speeds):
            self.pointer = 0

    def reset(self):
        self.pointer = 0
        self.dist = 0
        self.points = 0


racers = []

for line in data:
    words = line.split()
    speeds = [int(words[3])] * int(words[6]) + [0] * int(words[13])
    print(speeds)
    racers.append(Reindeer(words[0], speeds))

for i in range(2503):
    for r in racers:
        r.go()

maxDist = 0

for r in racers:
    if r.dist > maxDist:
        maxDist = r.dist

print(maxDist)

# part 2

for r in racers:
    r.reset()

for i in range(2503):
    for r in racers:
        r.go()
    maxDist = 0
    for r in racers:
        if r.dist > maxDist:
            maxDist = r.dist
    for r in racers:
        if r.dist == maxDist:
            r.points += 1

maxPoints = 0

for r in racers:
    if r.points > maxPoints:
        maxPoints = r.points

print(maxPoints)
