with open("Day3input.txt") as f:
    data = f.read()

x = 0
y = 0
visited = {(x, y)}

for c in data:
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == 'v':
        y += 1
    elif c == '^':
        y -= 1
    else:
        print("Illegal character in input ({})".format(c))

    visited.add((x, y))

print(len(visited))

# part 2

xs = 0
ys = 0
sVisited = {(xs, ys)}
xr = 0
yr = 0
rVisited = {(xr, yr)}

for i, c in enumerate(data):
    if i % 2 == 0:
        if c == '<':
            xs -= 1
        elif c == '>':
            xs += 1
        elif c == 'v':
            ys += 1
        elif c == '^':
            ys -= 1
        else:
            print("Illegal character in input ({})".format(c))

        sVisited.add((xs, ys))
    else:
        if c == '<':
            xr -= 1
        elif c == '>':
            xr += 1
        elif c == 'v':
            yr += 1
        elif c == '^':
            yr -= 1
        else:
            print("Illegal character in input ({})".format(c))

        rVisited.add((xr, yr))

print(len(sVisited | rVisited))
