from functools import reduce
from operator import mul

with open("Day24input.txt", "r") as f:
    data = f.readlines()

packets = []

for line in data:
    packets.append(int(line))

weight = sum(packets) / 3

lowest_package_count = 10**10  # current lowest package count
package_group = []  # the best group with the lowest package count
package_group_qe = 10**100  # current quantum entanglement


# it's slow and overcomplicated, but it works
def is_nth_in_group(n, group, left):
    global lowest_package_count
    global package_group
    global package_group_qe
    global packets
    global weight

    sum_group = sum(group)
    if sum_group == weight:
        qe = reduce(mul, group)
        if len(group) < lowest_package_count:
            lowest_package_count = len(group)
            package_group = group
            package_group_qe = qe
            print("found better: L{} {}   QE = {}".format(lowest_package_count, group, qe))
        elif len(group) == lowest_package_count:
            if qe < package_group_qe:
                package_group = group
                package_group_qe = qe
                print("found better qe: L{} {}   QE = {}".format(lowest_package_count, group, qe))
        else:
            return
    elif sum_group > weight:
        return
    else:  # we can add more
        if n + 1 <= len(packets):
            new_group = group[:]
            new_group.append(packets[n])
            new_left = left[:]
            new_left.remove(packets[n])
            is_nth_in_group(n + 1, group, left)
            is_nth_in_group(n + 1, new_group, new_left)


is_nth_in_group(0, [], packets)



