def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1 ):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

#[193136, 193223] имеет 6 делителей
for x in range(193136, 193223+1):
    d = div(x)
    if len(d) == 6:
        print(d)


