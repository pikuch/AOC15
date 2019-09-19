with open("Day2input.txt") as f:
    data = f.readlines()

area = 0
length = 0
for present in data:
    dims = present.split('x')
    numDims = list(map(lambda d: int(d), dims))
    # paper
    walls = [numDims[0]*numDims[1], numDims[1]*numDims[2], numDims[2]*numDims[0]]
    minWall = min(walls)
    area += 2*walls[0] + 2*walls[1] + 2*walls[2] + minWall
    # ribbons
    volume = numDims[0]*numDims[1]*numDims[2]
    numDims.remove(max(numDims))
    length += numDims[0]*2 + numDims[1]*2 + volume

print(area)
print(length)
