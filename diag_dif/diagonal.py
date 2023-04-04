arr = [ [-10, 3, 0,  5, -4],
        [2, -1,  0,  2, -8],
        [9, -2, -5,  6,  0],
        [9, -7,  4,  8, -2],
        [3,  7,  8, -5,  0]]


maind = 0
offd = 0
for i in range(0,len(arr)):
    maind += arr[i][i]
    for j in range(i,len(arr)):
        if i+j == len(arr) - 1:
            offd += arr[i][j] if i == j else  arr[i][j] + arr[j][i]
        print("i={}, j={}, main={}, off={}, dif={}".format(i, j, maind, offd, abs(maind - offd)))


print(abs(maind - offd))
