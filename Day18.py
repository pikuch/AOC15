#from PIL import Image
import numpy

with open("Day18input.txt") as f:
    data = f.readlines()

maxX = 100
maxY = 100

arr = numpy.zeros((maxX, maxY))
change = numpy.zeros((maxX, maxY))

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if j < maxY:
            arr[i, j] = 1 if c == "#" else 0


def neighbours(x, y):
    n = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if x + dx < 0 or x + dx > maxX-1:
                continue
            if y + dy < 0 or y + dy > maxY-1:
                continue
            if arr[x + dx, y + dy] == 1:
                n += 1
    return n


# part 2 - these 4 lines here and in the loop
arr[0, 0] = 1
arr[0, maxY-1] = 1
arr[maxX-1, 0] = 1
arr[maxX-1, maxY-1] = 1

for step in range(100):
    for x in range(maxX):
        for y in range(maxY):
            n = neighbours(x, y)
            if arr[x, y] == 1:
                if n == 2 or n == 3:
                    change[x, y] = 0
                else:
                    change[x, y] = -1
            else:
                if n == 3:
                    change[x, y] = 1
                else:
                    change[x, y] = 0
    arr = arr + change
    # part 2
    arr[0, 0] = 1
    arr[0, maxY-1] = 1
    arr[maxX-1, 0] = 1
    arr[maxX-1, maxY-1] = 1

#img = Image.fromarray(arr * 255)
#img.show()

print(arr.sum())
