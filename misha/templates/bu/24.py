
f = open('txt.txt').readline()

s, mx = [], 0
for i in range(len(f)):
    s.append(f[i])
    for j in range(i+1, len(f)):
        if f[j] not in s:
            s.append(f[j])
        else:
            if mx < len(s):
                mx = len(s)
            s = []
            break
    if len(s) == 26:
        break
print(mx)











