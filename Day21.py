with open("Day21input.txt") as f:
    data = f.readlines()

bossHP = int(data[0].split()[2])
bossDamage = int(data[1].split()[1])
bossArmor = int(data[2].split()[1])

playerHP = 100
playerDamage = 0
playerArmor = 0

weapons = [   # Cost  Damage  Armor
["Dagger",        8,     4,       0],
["Shortsword",   10,     5,       0],
["Warhammer",    25,     6,       0],
["Longsword",    40,     7,       0],
["Greataxe",     74,     8,       0]]

armor = [
["Leather",      13,     0,       1],
["Chainmail",    31,     0,       2],
["Splintmail",   53,     0,       3],
["Bandedmail",   75,     0,       4],
["Platemail",   102,     0,       5]]

rings = [
["Damage +1",    25,     1,       0],
["Damage +2",    50,     2,       0],
["Damage +3",   100,     3,       0],
["Defense +1",   20,     0,       1],
["Defense +2",   40,     0,       2],
["Defense +3",   80,     0,       3]]


def sim(bHP, bDamage, bArmor, pHP, pDamage, pArmor, deltaHP, deltaDamage, deltaArmor):
    pHP += deltaHP
    pDamage += deltaDamage
    pArmor += deltaArmor
    while True:
        bHP -= 1 if pDamage - bArmor < 1 else pDamage - bArmor
        if bHP <= 0:
            return True
        pHP -= 1 if bDamage - pArmor < 1 else bDamage - pArmor
        if pHP <= 0:
            return False


print(sim(bossHP, bossDamage, bossArmor, playerHP, playerDamage, playerArmor, 0, 0, 0))
