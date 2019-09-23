import json

with open("Day12input.txt") as f:
    data = f.read()

# the first part by brute force
digitsPlus = "-0123456789"
filtered = list(map(lambda c: ' ' if c not in digitsPlus else c, data))

filteredStr = "".join(filtered)
items = filteredStr.split()
numbers = map(lambda x: int(x), items)

print(sum(numbers))

# part 2


def remRed(jd):
    if isinstance(jd, dict):
        for k, v in jd.items():
            if k == "red" or v == "red":
                return None
        result = dict()
        for k, v in jd.items():
            result[k] = remRed(v)
        return result

    elif isinstance(jd, list):
        result = []
        for i in jd:
            result.append(remRed(i))
        return result
    else:
        return jd


jData = json.loads(data)

jClean = remRed(jData)

data = str(jClean)

filtered = list(map(lambda c: ' ' if c not in digitsPlus else c, data))

filteredStr = "".join(filtered)
items = filteredStr.split()
numbers = map(lambda x: int(x), items)

print(sum(numbers))
