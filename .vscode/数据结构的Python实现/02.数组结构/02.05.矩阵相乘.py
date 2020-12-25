#设计一个Python程序来实现两个可自行输入矩阵维数的矩阵相乘过程，并显示输出相乘的结果


def matrix_maltiply(arr_a, arr_b, arr_c, m, n, p):
    global c
    if m <= 0 or n <= 0 or p <= 0:
        print('错误：矩阵的维数m,n,p必须大于0！')
        return
    for i in range(m):
        for j in range(p):
            temp = 0
            for k in range(n):
                temp += int(arr_a[i * n + k]) * int(arr_b[k * p + j])
            arr_c[i * p + j] = temp


print('请输入矩阵a的维数(m,n):')
m = int(input('m= '))
n = int(input('n= '))
a = [None] * m * n
#声明大小为m*n的列表a

print('请输入矩阵a的各个元素：')
for i in range(m):
    for j in range(n):
        a[i * n + j] = input('a%d%d= ' % (i, j))

print('请输入矩阵b的维数(n,p):')
n = int(input('n= '))
p = int(input('p= '))
b = [None] * n * p
#声明大小为n*p的列表b

print('请输入矩阵b的各个元素：')
for i in range(n):
    for j in range(p):
        b[i * p + j] = input('b%d%d= ' % (i, j))

c = [None] * m * p
#声明大小为m*p的矩阵c

matrix_maltiply(a, b, c, m, n, p)

print('a*b 的结果为：')
for i in range(m):
    for j in range(p):
        print('%d' % c[i * p + j], end='\t')
    print()
