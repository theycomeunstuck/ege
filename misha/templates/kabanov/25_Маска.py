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


## 1?2*3%4. "%" - простое число
# prime_list = []
# for i in range
# for i in range(10**7):
#     if fnmatch(str(i), '1?2*3'):
#         for j in prime_list:
#             if len(s+str(j) + '4') <= 9:
#                 print(s + str(j) + '4')







