# 1
# from functools import lru_cache
# @lru_cache(None)
# def f(a,b):
#     if a+b >= 91: return 0
#     if a<b:  t = [f(a+2,b), f(a+5,b), f(a+15, b)]
#     else:    t = [f(a, b+2), f(a, b+5), f(a, b+15)]
#
#     n = [i for i in t if i <= 0]
#     if n: return -max(n)+1
#     else: return -max(t)
# s = 0
# for i in range(1,61): #(1,30) = 1-29
#     func = f(15,i)
#     if f(15, i) == -1 or func == -2 or func == -3:
#         print(i)
#         s += 1
# print(f'answer: {s}')



#2
# from functools import lru_cache
# @lru_cache(None)
# def f(a):
#     if a >= 45: return 0
#     t = [f(a+1), f(a+3)]
#
#     n = [i for i in t if i <= 0]
#     if n: return -max(n)+1
#     else: return -max(t)
# s = 0
# for i in range(1,46): #(1,30) = 1-29
#     func = f(i)
#     if func == -2 or func == -1:
#         print(i)
#         s += 1
# print(f'answer: {s}')
#
#
# 3
# from functools import lru_cache
# @lru_cache(None)
# def f(a, b):
#     if b+a >= 109: return 0
#     t = [f(a+7, b), f(a,b+7), f(a*3, b), f(a,b*3)]
#
#     n = [i for i in t if i <= 0]
#
#     if n: return -max(n)+1
#     else: return -max(t)
# s = 0
# for i in range(1,96): #(1,30) = 1-29
#     func = f(12, i)
#     if func == -2 or func == -1:
#         print(i)
#         s += 1
# print(f'answer: {s}')
#
#
#


