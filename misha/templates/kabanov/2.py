from itertools import *
"""Если дана вся таблица, кроме буковок"""
def f(x,y,z):
    return ((not x) and y and z) or ((not x) and (not z))

table = [(0,0,0), (1,0,0), (1,1,0)]

for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in table] == [1,1,1]:
        # print(p)
        pass


'''заполнение пустот'''
# from itertools import *
# def f(x,y,w,z):
#     return ((y<=x) or ((not z) and w)) == (w==x)
#
# for a in product([0,1],repeat=3):
#     table= [(a[0], 1,0,0), (0,0,0,1), (0,1,a[1],a[2])]
#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, r))) for r in table] == [1,1,1]:
#                 print(p)

from itertools import *
def f(x,y,z,w):
    return  (x== (not y)) <= (((x and w) == z))

for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    table = [(1,1,a1,a2),
             (1,1,a3,1),
             (a4,1,1,a5)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in table] == [0,0,0]:
                print(p)

'''число расстановок (сколькими способами можно поставить в соответствие переменные w,x,y,z столбцам
таблицы истинности функции?'''

from itertools import *
def f(x,y,w,z):
    return ((x == y) <= (z==w))

table = [(0,0,0,1),
         (1,1,1,0)]
k = 0
for p in permutations('xywz'):
    if [f(**dict(zip(p,r ))) for r in table] == [0,0]:
        k += 1
print(k)