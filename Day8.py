with open("Day8input.txt") as f:
    data = f.readlines()

codes = 0
chars = 0
encoded = 0
data2 = []
data3 = []
data4 = []

for s in data:
    codes += len(s)

print(data[4])

for s in data:
    count = s.count(r"\\")
    chars += count
    encoded += 2 * count
    data2.append(s.replace(r"\\", ""))

print(data2[4])

for s in data2:
    count = s.count(r"\"")
    chars += count
    encoded += 2 * count
    data3.append(s.replace(r"\"", ""))

print(data3[4])

for s in data3:
    count = s.count(r"\x")
    chars -= count
    encoded += count
    data4.append(s.replace(r"\x", ""))

print(data4[4])

for s in data4:
    count = len(s)
    chars += count-2
    encoded += 4

print("{} - {} = {}".format(codes, chars, codes - chars))
print(encoded)
