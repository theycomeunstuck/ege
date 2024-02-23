s = '0123456789abcde'
t = set()
for x in s:
    n = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if n % 14 == 0:
       t.add(x)
k = str(min(t))
print((int('123' + k + '5', 15) + int('1' + k + '233', 15)) / 14, t)



























