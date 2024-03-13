from functools import lru_cache
"""solution by by"""
@lru_cache(None)
def f(a, b):
    if a + b >= 68: return 0
    t = [f(a + 2, b), f(a, b + 2), f(a * 3, b), f(a, b * 3)]
    n = [i for i in t if i <= 0]
    if n: return -max(n) + 1
    else: return -max(t)


s = 0
for i in range(1, 60):  # 1-29
    if f(8, i) == 1:  # количество ходов, при которых ваня выигрывает первым ходом. ответ может быть 0
        print(i)
        s += 1
print(f'answer: {s}')


# "+" means petya / / "-" means vanya
# if (t[0], t[1]) == 1: steps = -1 (cause there is from a options which direct to win only
# /если сразу два пути ведут к победе)



