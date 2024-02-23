#Определите, наибольшее количество детей, которые придут в парк и
#покатаются на аттракционах за 24 часа и номер аттракциона, который займут последним.
f = open('fillers/26-1.txt')
k, n = f.readline().split() #аттракционы, колво детей
a = sorted([list(map(int, i.split())) for i in f])
print(a)
mx = 0
for j in range(int(k)):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            mx = max(mx, a[i][0])
            if i == 494: print(f'{t}\n', a)
    for i in l:
        a.pop(i)
print(f'count of clients: {(n-len(a))}\nlatest engaged time: {mx}')
"""f = open('file.txt')
k = int(f.readline()) #cell
n = int(f.readline()) #total clients count
a = sorted([list(map(int, i.split())) for i in f]) #sorted queue
c = 0 #sum engaged cells

'''for the found max time engage cell'''
mx = 0


for j in range(k):
    #modeling for the one cell
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]: #compare with the one last cell in list. cannot do t[i][1] cause there is some trouble
            t.append(a[i])
            l.append(i)
            mx = max(mx, a[i][0])
    for i in l:
        a.pop(i)

    print(f'client: {j}; {t}) #client, [clienttime, releasetime]')
print(f'count of clients: {(n-len(a))}\nlatest engaged time: {mx}')
"""