s = open('fillers/24-280.txt').readline()
l, m, kx, ky = 0, 0, 0, 0

for r in range(len(s)):
    if s[r] == 'X': kx += 1
    if s[r] == 'Y': ky += 1
    while kx > 1 or ky > 1:
        if s[l] == 'X': kx -=1
        if s[l] == 'Y': ky -=1
        l += 1
    if kx == 1 and ky == 1: m = max(m, r - l + 1)
print(m)