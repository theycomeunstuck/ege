'''Долгий по времени, но в 4 строчки!'''
from fnmatch import *
#* - любое кол-во символов (в том числе и пустая посл.)
#? - один любой символ
for x in range(0, 10**9, 17): #число % 17 == 0
    if fnmatch(str(x), '23?456?89'):
        print(x, x // 17 )



'''2 способ'''
for c1 in '0123456789':
    for c2 in '0123456789':
        a = int(f'23{c1}456{c2}89')
        if a % 17 == 0:
            print(a, a//17)

'''3 способ через itertools'''
from itertools import *

#кол-во в repeat зависит от /число не превышает 10**n
#repeat=n-1
#маска -- 12?345?67089?

for a1,a2,a3 in product('0123456789', repeat=3):
    s = int(f'12{a1}345{a2}67089{a3}')
    if s%206 == 0:
        print(s, s//206)


#2) маска -- 123?4*5679 до 10**12 (т.е. 11 символов)
ans = set()
for a1 in '0123456789':
    for l in 0,1,2,3:
        for x in product('0123456789', repeat=l):
            b = ''.join(x)
            s = int(f'123{a1}4{b}5679')
            if s%4013==0: ans.add(s)
for s in sorted(ans):
    print(s, s // 4013)


## 1?2*3%4. "%" - простое число
# prime_list = []
# for i in range
# for i in range(10**7):
#     if fnmatch(str(i), '1?2*3'):
#         for j in prime_list:
#             if len(s+str(j) + '4') <= 9:
#                 print(s + str(j) + '4')







