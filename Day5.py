with open("Day5input.txt") as f:
    data = f.readlines()


def isNice(ss):
    # vowel count rule check
    vowelCount = 0
    vowelCount += ss.count('a')
    vowelCount += ss.count('e')
    vowelCount += ss.count('i')
    vowelCount += ss.count('o')
    vowelCount += ss.count('u')
    if vowelCount < 3:
        return False

    # double letter rule check
    doubleCount = 0
    for i in range(len(ss)-1):
        if ss[i] == ss[i + 1]:
            doubleCount += 1
    if doubleCount == 0:
        return False

    # forbidden substrings rule check
    if ss.find('ab') > -1:
        return False
    if ss.find('cd') > -1:
        return False
    if ss.find('pq') > -1:
        return False
    if ss.find('xy') > -1:
        return False

    # otherwise it's a nice string
    return True


niceCounter = 0
for s in data:
    if isNice(s):
        niceCounter += 1

print(niceCounter)


# part 2


def isNice2(ss):
    # repeated pair rule check
    repeated = 0
    for i in range(len(ss) - 1):
        if ss.count(ss[i:i+2]) > 1:
            repeated += 1
            break
    if repeated == 0:
        return False

    # split pair rule check
    for i in range(len(ss) - 2):
        if ss[i] == ss[i+2]:
            return True

    return False


niceCounter = 0
for s in data:
    if isNice2(s):
        niceCounter += 1

print(niceCounter)
