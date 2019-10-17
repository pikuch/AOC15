with open("Day23input.txt", "r") as f:
    data = f.readlines()

program = []

for line in data:
    clean_line = line.replace(",", "")
    command = clean_line.split()
    program.append(command)


def run(prog):
    a = 0  # part 2: a = 1
    b = 0
    ptr = 0

    while True:
        if ptr < 0 or ptr >= len(prog):
            break
        cmd = prog[ptr]
        if cmd[0] == "hlf":
            if cmd[1] == "a":
                a = a // 2
                ptr += 1
            elif cmd[1] == "b":
                b = b // 2
                ptr += 1
            else:
                return "ERROR: illegal register name at {}: {}".format(ptr, str(cmd))
        elif cmd[0] == "tpl":
            if cmd[1] == "a":
                a *= 3
                ptr += 1
            elif cmd[1] == "b":
                b *= 3
                ptr += 1
            else:
                return "ERROR: illegal register name at {}: {}".format(ptr, str(cmd))
        elif cmd[0] == "inc":
            if cmd[1] == "a":
                a += 1
                ptr += 1
            elif cmd[1] == "b":
                b += 1
                ptr += 1
            else:
                return "ERROR: illegal register name at {}: {}".format(ptr, str(cmd))
        elif cmd[0] == "jmp":
            ptr += int(cmd[1])
        elif cmd[0] == "jie":
            if cmd[1] == "a":
                if a % 2 == 0:
                    ptr += int(cmd[2])
                else:
                    ptr += 1
            elif cmd[1] == "b":
                if b % 2 == 0:
                    ptr += int(cmd[2])
                else:
                    ptr += 1
            else:
                return "ERROR: illegal register name at {}: {}".format(ptr, str(cmd))
        elif cmd[0] == "jio":
            if cmd[1] == "a":
                if a == 1:
                    ptr += int(cmd[2])
                else:
                    ptr += 1
            elif cmd[1] == "b":
                if b == 1:
                    ptr += int(cmd[2])
                else:
                    ptr += 1
            else:
                return "ERROR: illegal register name at {}: {}".format(ptr, str(cmd))
        else:
            return "ERROR: illegal instruction at {}: {}".format(ptr, str(cmd))

    return b


result = run(program)

print(result)
