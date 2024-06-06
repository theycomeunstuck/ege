#метод двух указателей. https://www.youtube.com/watch?v=lx7FFGuoCjc


'''
4524. определите максимальное количество идущих подряд символов, среди которых не более одной точки. /aaaa.bbbbbbbbb.cc.dd
'''

#24
s = open('txt.txt').readline()
l, m, k = 0, 0, 0
for r in range(len(s)):
    if s[r] == '.': k +=1
    while k > 1:
        if s[l] == '.': k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)


'''
7193. файл 24-280.txt содержит только заглавные буквы латинского алфавита. Определите максимальное количество идущих подряд символов,
 среди которых буквы X и Y встречаются ровно по одному разу.
'''


s = open('24-280.txt').readline()
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


'''
6674. (ЕГЭ-2023) файл 24-263.txt содержит только заглавные буквы латинского алфавита. 
Определите минимальную длину подстроки, в которой символ Z встречается не менее 120 раз.
'''


s = open('24-263.txt').readline()
kz, l = 0, 0
m = 10000

for r in range(len(s)):
    if s[r] == 'Z': kz += 1
    while kz >= 120:
        if s[l] == 'Z': kz -= 1
        l += 1
        if kz == 120: m = min(m, r-l+1)
print(m)


'''
6182. (Д. Статный) файл 24-251.txtсодержит только латинские заглавные буквы A...Z и десятичные цифры. 
Определите максимальную длину подстроки, 
которая ограничена с одной стороной буквой A, а с другой – D и не содержит других букв A и D внутри.

'''


s = open('24-251.txt').readline()
l,m = 0,0

for r in range(len(s)):
    if s[r] == 'A' or s[r] == 'D':
        if s[r] == 'A' and s[r] == 'D' or s[l] == 'D' and s[r] == 'A':
            m = max(m, r-l+1)
        l = r

print(m)


'''
6053. файл 24-241.txt содержит только латинские буквы A, B, C, D, E, F, O. 
Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой O,
а между двумя последовательными буквами O содержит не более двух букв F и произвольное количество других букв.
'''

s = open('24-241.txt').readline()
l, m, kf = 0, 0, 0
#l = s.find('O') #optimization
#for r in range(l, len(s)):
for r in range(len(s)):
    if s[r] == 'F': kf += 1
    if s[r] == 'O':
        if kf > 2:
            l = r
        kf = 0
    if s[r] == 'O' and s[l] == 'O':
        m = max(m, r-l+1)

print(m)


'''
4753. файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов. 
Определите максимальное количество идущих подряд символов, среди которых нет гласных букв (символов A, E, I, O, U, Y), но есть не менее 6 точек.
'''


s = open('24-181.txt').readline()
l,m,k = 0,0,0

for r in range(len(s)):
    if s[r] in 'AEIOUY':
        l = r + 1
        k = 0
    if s[r] == '.':
        k += 1
    if k >= 6:
        m = max(m, r-l+1)

print(m)


'''
5253. (М. Шагитов)  файл 24-208.txt содержит строку из десятичных цифр, всего не более чем из 106 символов.
 Определите максимальное количество идущих подряд символов, 
 среди которых комбинация символов 2022 повторяется не более четырёх раз.
'''


s = open('24-208.txt').readline()
l,m,k2022 = 0,0,0

for r in range(3, len(s)):
    if s[r-3] + s[r-2] + s[r-1] + s[r] == '2022': k2022 += 1

    while k2022 > 4:
        if s[l]+s[l+1]+s[l+2]+s[l+3] == '2022':
            k2022 -= 1
        l += 1
    m = max(m,r-l+1)

print(m)




