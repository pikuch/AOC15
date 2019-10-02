with open("Day17input.txt") as f:
    data = f.readlines()

containers = [int(x) for x in data]


def combinations_with(containers, pos, sum_so_far, targeted_sum, containers_used, containers_used_list):
    if sum_so_far > targeted_sum:
        return 0
    elif sum_so_far == targeted_sum:
        containers_used_list.append(containers_used)
        return 1
    else:
        if pos < len(containers):
            return combinations_with(containers, pos+1, sum_so_far + containers[pos], targeted_sum, containers_used+1, containers_used_list) + \
                   combinations_with(containers, pos+1, sum_so_far, targeted_sum, containers_used, containers_used_list)
        else:
            return 0


targeted_sum = 150
containers_used = 0
containers_used_list = []
counter = combinations_with(containers, 0, 0, targeted_sum, containers_used, containers_used_list)

print(counter)
print(containers_used_list.count(min(containers_used_list)))
