with open("Day20input.txt") as f:
    data = f.readlines()

# let's calculate everything without multiplying by 10
n = int(data[0]) // 10

houses = [0]*(n // 2)

for i in range(1, len(houses)):
    for j in range(i, n // 2, i):
        houses[j] += i

for i in range(1, len(houses)):
    if houses[i] >= n:
        print(i)
        break

# part 2

n = int(data[0]) // 11

houses = [0]*(n // 2)

for i in range(1, len(houses)):
    counter = 0
    for j in range(i, n // 2, i):
        houses[j] += i
        counter += 1
        if counter >= 50:
            break

for i in range(1, len(houses)):
    if houses[i] >= n:
        print(i)
        break
