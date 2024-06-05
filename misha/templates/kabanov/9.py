f = open('09.txt') #ctrl + a в excel`е и в блокнотик ctrl+s
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if True: #условие
        k += 1
print(k)