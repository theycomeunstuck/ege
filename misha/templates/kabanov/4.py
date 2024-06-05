#1) перебор слов -- если есть повторяющиеся элементы
leto = 'ЛЕТО'
from itertools import *
s = 0
for x in product('ЛТ', leto, leto, leto):
# for x in product(leto, repeat=6):
    s += 1
print(s)

#2) переставовка -- нет повтор. элементов (сколько существует чисел?)
k = 0
from itertools import *
for x in set(permutations('КАЛИЙ')):
# for x in permutations('123', 5): #-- 5 - length
# for x in set(permutations("АССАСИН")):
    s = ''.join(x)
    #!
    if s[0] != 'Й' and 'ИА' not in s:
        k += 1
#4) Всe n-буквенные слова записаны в алф. порядке. укажите слово на Х месте
k = 0
for x in product(sorted('АКРУ'), repeat=5):
    s = ''.join(x)
    k += 1
    if k == 150:
        print(s)

# 3) перестановка с повторяющимися буквами ("АССАСИН")
# for x in set(permutations("АССАСИН")):
#     pass

# 3)
k = 0

for a in 'ЛТ':
    for b in leto:
        for c in leto:
            for d in leto:
                k += 1
print(k)

'''
remarks

число не может начинаться с 0



'''

# "колун" нет двух согл или двух гл подряд и буквы не могут повторяться
# d = 'КОЛУН'
#
# from itertools import *
# k =0
# for x in permutations(d):
#     s = ''.join(x)
#     s = s.replace('Л',"К").replace('Н',"К").replace('У',"О")
#     if 'КК' not in s and 'ОО' not in s:
#         k += 1
# print(k)