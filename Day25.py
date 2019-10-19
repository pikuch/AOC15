import string

with open("Day25input.txt", "r") as f:
    data = f.read()

filtered = ""

for c in data:
    if c in string.digits:
        filtered += c
    else:
        filtered += " "

words = filtered.split()

row = int(words[0])
col = int(words[1])

n = (row + col - 2) * (row + col - 1) / 2 + col

print("row: {} col: {} element: {}".format(row, col, n))


def nth_hash(x, n):
    while n > 1:
        x *= 252533
        x %= 33554393
        n -= 1
    return x


print(nth_hash(20151125, n))
