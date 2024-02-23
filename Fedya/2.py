"""
s = '0123456789ab'
s1 = '0123456789abcdefghi'
a =[]
b = []
c = set()
for x in s:
    for y in s1:
        k = 0
        n = int('5' + x + '9' + x + '4', 12) + int('7' + x + x + '6', 14) + int('5' + '5' + x + x + '8', 16) - int('3' + y + x + '7', 19)
        for i in  range(1, n+1):
            if (n % i == 0):
                k += 1
                if k == 3:
                    break
        if k == 2:
            a.append(x)
            b.append(y)
            c.add(int(x, 12) * int(y, 19))
print(a)
print(b)
print(max(c))
"""
s = '0123456789ab'
s1 = '0123456789abcdefghi'
a =[]
b = []
c = set()
for x in s:
    for y in s1:
        k = 0
        n = int('5' + x + '9' + x + '4', 12) + int('7' + x + x + '6', 14) + int('5' + '5' + x + x + '8', 16) - int('3' + y + x + '7', 19)
        for i in  range(2, n):
            if (n % i == 0):
                k += 1
                if k == 1:
                    break
        if k == 0:
            a.append(x)
            b.append(y)
            c.add(int(x, 12) * int(y, 19))
print(a)
print(b)
print(max(c))





















