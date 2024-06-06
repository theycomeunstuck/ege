a = [int(x) for x in open('file.txt')]
# ans_mass = []
# ans = [x for x in a if x % 3 == 0 and x % 7 != 0 and x % 19 != 0 and  x % 17 != 0 and x % 27 != 0]
# # for i in range(len(a)):
# #     if a[i] % 3 == 0 and a[i] % 7 != 0 and a[i] % 19 != 0 and a[i] % 17 != 0 and a[i] % 27 != 0:
# #         ans_mass.append(a[i])
#
# print(len(ans), max(ans))

'''пары'''
ans = []
''' пары = -1
    тройки = -2 '''
for i in range(len(a)-1):
    if abs(a[i])%10 == 7 or abs(a[i+1])%10 == 7:
        ans.append(a[i]+a[i+1]) #sum

'''тройки'''
for i in range(len(a)-2):
    a = a[i]
    b = a[i+1]
    c = a[i+2]

