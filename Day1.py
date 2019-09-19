with open("Day1input.txt") as f:
    data = f.read()

floor = 0
for c in data:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

print(floor)

# part 2
floor = 0
for i, c in enumerate(data):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        print(i+1)
        break
