#设计一个Python程序实现一个4*4二维数组的转置
arr_a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=4
arr_b=[[None]*n for row in range(n)] #声明一个4*4数组为转置矩阵

print('原矩阵为：')
#打印原矩阵
for i in range(n):
    for j in range(n):
        print('%d'%arr_a[i][j],end='\t')
    print()

#进行转置矩阵的操作
for i in range(n):
    for j in range(n):
        arr_b[i][j]=arr_a[j][i]

#打印转置后的矩阵
print('转置矩阵为：')
for i in range(n):
    for j in range(n):
        print('%d'%arr_b[i][j],end='\t')
    print()

    





