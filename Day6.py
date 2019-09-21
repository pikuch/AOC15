# from PIL import Image
import numpy

with open("Day6input.txt") as f:
    data = f.readlines()

arr = numpy.zeros((1000, 1000))


def switch(op, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if op == 'on':
                arr[x, y] = 1
            elif op == 'off':
                arr[x, y] = 0
            else:
                arr[x, y] = 1 - arr[x, y]


for s in data:
    words = s.split()
    if words[0] == "toggle":
        x1y1 = words[1].split(',')
        x2y2 = words[3].split(',')
        switch('t', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    elif words[1] == "on":
        x1y1 = words[2].split(',')
        x2y2 = words[4].split(',')
        switch('on', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    elif words[1] == "off":
        x1y1 = words[2].split(',')
        x2y2 = words[4].split(',')
        switch('off', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    else:
        print("illegal command!")

print(arr.sum())

# img = Image.fromarray(arr*255)
# img.show()

# part 2

arr = numpy.zeros((1000, 1000))


def switch2(op, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if op == 'on':
                arr[x, y] += 1
            elif op == 'off':
                if arr[x, y] > 0:
                    arr[x, y] -= 1
            else:
                arr[x, y] += 2


for s in data:
    words = s.split()
    if words[0] == "toggle":
        x1y1 = words[1].split(',')
        x2y2 = words[3].split(',')
        switch2('t', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    elif words[1] == "on":
        x1y1 = words[2].split(',')
        x2y2 = words[4].split(',')
        switch2('on', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    elif words[1] == "off":
        x1y1 = words[2].split(',')
        x2y2 = words[4].split(',')
        switch2('off', (int(x1y1[0]), int(x1y1[1])), (int(x2y2[0]), int(x2y2[1])))
    else:
        print("illegal command!")

print(arr.sum())

# img = Image.fromarray(arr)
# img.show()
