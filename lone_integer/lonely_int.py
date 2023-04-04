def lonelyinteger(a):
    if len(a) == 1: return a[0]
    b = [0] * 100 # se esse numero for mto grande, vale mais a pena pegar numero a numero e conferir, talvez
    for i in a:
        b[i] += 1
    for i in range(0,len(b)):
        if b[i] == 1:
            return i


arr = [15, 60, 74, 1, 94, 93, 28, 48, 70, 98, 45, 94, 42, 45, 48 ,1, 72 ,9, 24, 93 ,41 ,70 ,60, 28, 11 ,20, 72, 35 ,11, 98 ,31 ,74 ,31, 41, 9 ,42, 20, 35, 24]

print(lonelyinteger(arr))
