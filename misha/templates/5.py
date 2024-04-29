
#<=10
def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x = x // 3
    return s
#>10
def cc2(x):
    s = ''
    d = '0123456789abcdefghiij' #i tak dalee
    while x > 0:
        s = d[x%12] + s
        x = x//12
    return s


