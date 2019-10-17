with open("Day22input.txt") as f:
    data = f.readlines()

boss_HP = int(data[0].split()[2])
boss_damage = int(data[1].split()[1])

player_HP = 50
player_mana = 500

least_spent_mana = 10**10

spells = [  # name     cost  damage healing   armor    mana    time
    ["Missile",          53,      4,     0,      0,      0,      1],
    ["Drain",            73,      2,     2,      0,      0,      1],
    ["Shield",          113,      0,     0,      7,      0,      6],
    ["Poison",          173,      3,     0,      0,      0,      6],
    ["Recharge",        229,      0,     0,      0,    101,      5]]


def find_least_spent_mana(boss_HP, player_HP, is_player_turn, mana, spent_mana, timer_0, timer_1, timer_2, timer_3, timer_4):
    global least_spent_mana
    player_shield = 0

    if spent_mana > least_spent_mana:
        return

    # part 2
    if is_player_turn:
        player_HP -= 1
        if player_HP <= 0:
            return
    #

    if timer_0:
        boss_HP -= 4
        timer_0 -= 1
        if boss_HP <= 0:
            if spent_mana < least_spent_mana:
                least_spent_mana = spent_mana
                print(least_spent_mana)
            return

    if timer_1:
        boss_HP -= 2
        player_HP += 2
        timer_1 -= 1
        if boss_HP <= 0:
            if spent_mana < least_spent_mana:
                least_spent_mana = spent_mana
                print(least_spent_mana)
            return

    if timer_2:
        player_shield = 7
        timer_2 -= 1

    if timer_3:
        boss_HP -= 3
        timer_3 -= 1
        if boss_HP <= 0:
            if spent_mana < least_spent_mana:
                least_spent_mana = spent_mana
                print(least_spent_mana)
            return

    if timer_4:
        mana += 101
        timer_4 -= 1

    if is_player_turn:
        available_spell_count = 0
        if not timer_0 and mana >= 53:
            available_spell_count += 1
            find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana - 53, spent_mana + 53,
                                  timer_0 + 1, timer_1, timer_2, timer_3, timer_4)
        if not timer_1 and mana >= 73:
            available_spell_count += 1
            find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana - 73, spent_mana + 73,
                                  timer_0, timer_1 + 1, timer_2, timer_3, timer_4)
        if not timer_2 and mana >= 113:
            available_spell_count += 1
            find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana - 113, spent_mana + 113,
                                  timer_0, timer_1, timer_2 + 6, timer_3, timer_4)
        if not timer_3 and mana >= 173:
            available_spell_count += 1
            find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana - 173, spent_mana + 173,
                                  timer_0, timer_1, timer_2, timer_3 + 6, timer_4)
        if not timer_4 and mana >= 229:
            available_spell_count += 1
            find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana - 229, spent_mana + 229,
                                  timer_0, timer_1, timer_2, timer_3, timer_4 + 5)
        if not available_spell_count:
            return
    else:  # boss turn
        damage = boss_damage - player_shield
        if damage < 1:
            damage = 1
        player_HP -= damage
        if player_HP <= 0:
            return
        find_least_spent_mana(boss_HP, player_HP, 1 - is_player_turn, mana, spent_mana,
                              timer_0, timer_1, timer_2, timer_3, timer_4)


find_least_spent_mana(boss_HP, player_HP, 1, player_mana, 0, 0, 0, 0, 0, 0)

print("^ minimum mana needed")
