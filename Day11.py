import string

with open("Day11input.txt") as f:
    data = f.read()

data = list(data)


def findNext(pwd):
    result = pwd
    pos = len(pwd)-1
    while True:
        if pos < 0:
            break
        if result[pos] == 'z':
            result[pos] = 'a'
            pos -= 1
        else:
            result[pos] = chr(ord(result[pos])+1)
            break

    return result


def goodEnough(pwd):
    # no confusing letters rule
    if 'i' in pwd:
        return False
    if 'o' in pwd:
        return False
    if 'l' in pwd:
        return False
    # at least two different pairs rule
    pairs = 0
    for c in string.ascii_lowercase:
        for i in range(len(pwd)-1):
            if c == pwd[i] == pwd[i+1]:
                pairs += 1
                break
    if pairs < 2:
        return False
    # increasing letters rule
    for i in range(len(pwd)-2):
        if pwd[i] == chr(ord(pwd[i+1])-1) == chr(ord(pwd[i+2])-2):
            return True

    return False


data = findNext(data)
while not goodEnough(data):
    data = findNext(data)

print("".join(data))

data = findNext(data)
while not goodEnough(data):
    data = findNext(data)

print("".join(data))
