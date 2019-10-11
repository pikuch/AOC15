with open("Day19inputB.txt") as f:
    data = f.readlines()

replacements = []

for line in data[:-2]:
    words = line.split()
    replacements.append([words[0], words[2]])

molecule = data[-1]
products = set()

for rule in replacements:
    start = 0
    place = molecule.find(rule[0], start)
    while place >= 0:
        first_part = molecule[:place]
        second_part = molecule[place:]
        new_molecule = first_part + second_part.replace(rule[0], rule[1], 1)
        products.add(new_molecule)
        start = place + len(rule[0])
        place = molecule.find(rule[0], start)

print(len(products))

# part 2


def try_shorten(replacements, shorties_by_steps, steps):

    while True:
        mol = shorties_by_steps[steps-1]
        rule_string = ""
        for rule in replacements:
            place = mol.find(rule[1])
            if place == -1:
                continue
            new_mol = mol.replace(rule[1], rule[0], 1)
            if new_mol == "e":
                return steps
            else:
                shorties_by_steps.append(new_mol)
                rule_string = rule[1] + " => " + rule[0]
                break

        # print("step {}: {} {}  [length:{}]".format(steps, rule_string, shorties_by_steps[steps], len(shorties_by_steps[steps])))
        steps += 1


shorties_by_steps = [molecule]

min_steps = try_shorten(replacements, shorties_by_steps, 1)

print(min_steps)
