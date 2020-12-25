#设计一个Python程序，将右上三角矩阵压缩为一维矩阵
global arr_size  #矩阵的维数大小
arr_size = 5

#一维数组的数组声明
num = int(arr_size * (1 + arr_size) / 2)
b = [None] * num


def get_value(i, j):
    index = int(arr_size * i + j - i * (i + 1) / 2)
    return b[index]


#右上三角矩阵的内容
a = [[7, 8, 12, 21, 9], [0, 5, 14, 17, 6], [0, 0, 7, 23, 24],
     [0, 0, 0, 32, 19], [0, 0, 0, 0, 8]]

print('=' * 20)
print('上三角矩阵：')
for i in range(arr_size):
    for j in range(arr_size):
        print('%d' % a[i][j], end='\t')
    print()

#将右上三角矩阵压缩为一维数组
index = 0
for i in range(arr_size):
    for j in range(i, arr_size):
        b[index] = a[i][j]
        index += 1
print('=' * 20)

print('以一维数组的方式表示为：')
print('[', end='')
for i in range(arr_size):
    for j in range(i, arr_size):
        print('%d' % get_value(i, j), end=' ')
print(']')
