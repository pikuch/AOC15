from hashlib import md5

with open("Day4input.txt") as f:
    data = f.read()

h = ""
n = 0
while h[:5] != "00000":
    n += 1
    h = md5((data+str(n)).encode("utf-8")).hexdigest()

print(n, h)

# part 2
h = ""
n = 0
while h[:6] != "000000":
    n += 1
    h = md5((data+str(n)).encode("utf-8")).hexdigest()

print(n, h)
