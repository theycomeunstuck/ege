# Число простое, если у него нет делителей на промежутке [2, x**0.5]
def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1) ) #простые числа


#     18
# 1 2 3 6 9 18
# делители можно разбить на пары (1*18=18; 2*9=18; 3*6=18)
# - достаточно найти половину делителей

# если число является квадратом, то у него нечётное кол-во делителей
#    перебор до sqrt(x) == x**0.5

def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1 ):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)




for x in range(193136, 193223+1): #[193136, 193223]
    #d = [i for i in div(x) if !условие! ] -- только !какие-то! делители в списке
    d = div(x)
    if True:
        print(d)



#Нетривиальные делители - делители, не равные 1 и самому X
#Основная теорема арифметики - ( (p**n) + 1 = кол-во делителей)S


#d = [i for i in div(x) if i%2 == 0] -- только чётные делители в списке


#viebon
    #return sorted({i for d in range(1, int(x**0.5) + 1) if x % d == 0 for i in (d, x//d)})
