with open("Day15input.txt") as f:
    data = f.readlines()


def gen(result_list, current_buckets, bucket_n, left):
    if bucket_n == len(current_buckets)-1:
        current_buckets[bucket_n] = left
        result_list.append(current_buckets[:])
    else:
        for i in range(left+1):
            current_buckets[bucket_n] = i
            gen(result_list, current_buckets, bucket_n + 1, left - i)


def generate(buckets, maximum):
    result_list = []
    current_buckets = [0]*buckets
    gen(result_list, current_buckets, 0, maximum)
    return result_list


ingredients = []

for line in data:
    words = line.replace(",", " ").split()
    props = {words[1]: int(words[2]), words[3]: int(words[4]), words[5]: int(words[6]), words[7]: int(words[8]), words[9]: int(words[10])}
    ingredients.append(props)

possibilities = generate(len(data), 100)

max_score = 0
max_score_500 = 0

for p in possibilities:
    capacity = 0
    for i, amount in enumerate(p):
        capacity += amount * ingredients[i]["capacity"]
    if capacity < 0:
        capacity = 0
    durability = 0
    for i, amount in enumerate(p):
        durability += amount * ingredients[i]["durability"]
    if durability < 0:
        durability = 0
    flavor = 0
    for i, amount in enumerate(p):
        flavor += amount * ingredients[i]["flavor"]
    if flavor < 0:
        flavor = 0
    texture = 0
    for i, amount in enumerate(p):
        texture += amount * ingredients[i]["texture"]
    if texture < 0:
        texture = 0
    calories = 0
    for i, amount in enumerate(p):
        calories += amount * ingredients[i]["calories"]
    if calories < 0:
        calories = 0
    score = capacity * durability * flavor * texture
    if score > max_score:
        max_score = score
    if score > max_score_500 and calories == 500:
        max_score_500 = score

print(max_score)
print(max_score_500)
