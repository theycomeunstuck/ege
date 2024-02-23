from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if b+a >= 111: return 0
    t = [f(a+5, b), f(a,b+5), f(a*4, b), f(a,b*4)]
    n = [i for i in t if i <= 0]
    if n: return -max(n)+1
    else: return -max(t)
s = 0
for i in range(1,99): #(1,30) = 1-29
    func = f(12, i)
    if func==2:
        print(i)
        s += 1
print(f'answer: {s}')












