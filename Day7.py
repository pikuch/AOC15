class Bits16:

    def __init__(self):
        self.bits = [0 for _ in range(16)]

    def __str__(self):
        return str(self.bits).strip("[]")

    def toInt(self):
        n = 0
        for i, b in enumerate(self.bits):
            n += b*2**i
        return n

    def fromInt(self, integer):
        for i in range(16):
            self.bits[i] = integer % 2
            integer //= 2
        return self

    def doNot(self):
        result = Bits16()
        for i in range(16):
            result.bits[i] = 1 - self.bits[i]
        return result

    def doAnd(self, other):
        result = Bits16()
        for i in range(16):
            result.bits[i] = 1 if (self.bits[i] > 0 and other.bits[i] > 0) else 0
        return result

    def doOr(self, other):
        result = Bits16()
        for i in range(16):
            result.bits[i] = 1 if (self.bits[i] > 0 or other.bits[i] > 0) else 0
        return result

    def doLshift(self, times):
        while times > 0:
            for i in range(15, 0, -1):
                self.bits[i] = self.bits[i-1]
            self.bits[0] = 0
            times -= 1
        return self

    def doRshift(self, times):
        while times > 0:
            for i in range(15):
                self.bits[i] = self.bits[i+1]
            self.bits[15] = 0
            times -= 1
        return self


def solve(line, part):
    result = Bits16()
    a = Bits16()
    b = Bits16()

    # the solution to part 2
    if part == 2:
        if line[-1] == 'b':
            return result.fromInt(3176)

    # simple assignment
    if len(line) == 3:
        if line[0].isdigit():
            return result.fromInt(int(line[0]))
        else:
            return False
    # NOT
    elif len(line) == 4:
        if line[1].isdigit():
            return result.fromInt(int(line[1])).doNot()
        else:
            return False
    # other operations
    elif len(line) == 5:
        if line[1] == "OR":
            if line[0].isdigit() and line[2].isdigit():
                return a.fromInt(int(line[0])).doOr(b.fromInt(int(line[2])))
            else:
                return False
        if line[1] == "AND":
            if line[0].isdigit() and line[2].isdigit():
                return a.fromInt(int(line[0])).doAnd(b.fromInt(int(line[2])))
            else:
                return False
        if line[1] == "LSHIFT":
            if line[0].isdigit() and line[2].isdigit():
                return a.fromInt(int(line[0])).doLshift(int(line[2]))
            else:
                return False
        if line[1] == "RSHIFT":
            if line[0].isdigit() and line[2].isdigit():
                return a.fromInt(int(line[0])).doRshift(int(line[2]))
            else:
                return False
    else:
        print("illegal data!")

    return False


with open("Day7input.txt") as f:
    data = f.readlines()

symbols = dict()
wires = []

for s in data:
    wires.append(s.split())

while len(wires) > 0:
    # find a solvable wire
    for w in wires:
        if isinstance(w[-1], int):
            continue
        s = solve(w, 2)
        if type(s) == Bits16:
            symbols[w[-1]] = s.toInt()
            print("{} = {}".format(w[-1], s.toInt()))
            # update the wires with new info
            newWires = []
            for wire in wires:
                if wire != w:
                    newWires.append([str(s.toInt()) if item == w[-1] else item for item in wire])
            wires = newWires
            break

print(symbols['a'])
