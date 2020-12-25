#设计一个Python程序利用三项式（3-tuple）数据结构，来压缩6*6稀疏矩阵，以减少内存不必要的浪费
#相比书中的代码区别：
#1.先统计非零元素个数，确定压缩矩阵大小
#2.增加稀疏矩阵的转置的算法实现

nonzero = 0  #记录6*6矩阵中的非零项的个数
#声明稀疏矩阵
sparse_a = [[15, 0, 0, 22, 0, -15], [0, 11, 3, 0, 0, 0], [0, 0, 0, -6, 0, 0],
            [0, 0, 0, 0, 0, 0], [91, 0, 0, 0, 0, 0], [0, 0, 28, 0, 0, 0]]
#遍历打印出稀疏矩阵的各个元素，并统计非零元素个数
for i in range(6):
    for j in range(6):
        print('%d' % sparse_a[i][j], end='\t')
        if sparse_a[i][j]:
            nonzero += 1
    print()

#声明压缩矩阵
compress_a = [[None] * 3 for row in range(nonzero + 1)]
#开始压缩稀疏矩阵
compress_a[0][0] = 6
compress_a[0][1] = 6
compress_a[0][2] = nonzero
temp = 1
for i in range(6):
    for j in range(6):
        if sparse_a[i][j]:
            compress_a[temp][0] = i
            compress_a[temp][1] = j
            compress_a[temp][2] = sparse_a[i][j]
            temp += 1

#打印压缩矩阵的各个元素
print('稀疏矩阵压缩后的内容：')
for i in range(nonzero + 1):
    for j in range(3):
        print('%d' % compress_a[i][j], end='\t')
    print()

#稀疏矩阵的转置
