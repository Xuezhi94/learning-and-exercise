#矩阵加法
a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
n = 3
c = [[None] * n for row in range(n)]
for i in range(n):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]
print('矩阵a与b相加的结果为：')
for i in range(n):
    for j in range(n):
        print('%d' % c[i][j], end='\t')
    print()
