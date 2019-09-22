with open("Day10input.txt") as f:
    data = f.read()


# look and say
def las(s):
    result = ""
    pos = 0
    series = 1
    while pos < len(s):
        if pos+1 < len(s):
            if s[pos] == s[pos+1]:
                series += 1
                pos += 1
            else:
                result += str(series)
                result += str(s[pos])
                series = 1
                pos += 1
        else:
            result += str(series)
            result += str(s[pos])
            pos += 1

    return result


for i in range(50):
    data = las(data)

print(len(data))