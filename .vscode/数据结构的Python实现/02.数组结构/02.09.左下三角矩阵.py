#设计一个Python程序，将左下三角矩阵压缩为一维数组
global arr_size  #矩阵维数大小
arr_size = 5

#一维数组的数组声明
num = int(arr_size * (arr_size + 1) / 2)
b = [None] * num


def get_value(i, j):
    index = int(i * (i + 1) / 2 + j)
    return b[index]


#下三角矩阵的内容
a = [[76, 0, 0, 0, 0], [54, 51, 0, 0, 0], [23, 8, 26, 0, 0],
     [43, 35, 28, 18, 0], [12, 9, 14, 35, 46]]

print('=' * 40)
print('下三角矩阵为：')
for i in range(arr_size):
    for j in range(arr_size):
        print('%d' % a[i][j], end='\t')
    print()

#将下三角矩阵压缩为一维数组
index = 0
for i in range(arr_size):
    for j in range(i + 1):
        b[index] = a[i][j]
        index += 1

print('=' * 40)
print('以一维数组的方式表示为：')
print('[', end='')
for i in range(arr_size):
    for j in range(i + 1):
        print('%d' % get_value(i,j), end=' ')
print(']')
