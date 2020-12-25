n = 2
#声明2*2的数组arr并将所有元素设置为None
arr = [[None] * n for row in range(n)]
print('|a1 b1|')
print('|a2,b2|')
arr[0][0] = input('please input a1:')
arr[0][1] = input('please input b1:')
arr[1][0] = input('please input a2:')
arr[1][1] = input('please input b2:')
#求二阶行列式的值
result = int(arr[0][0]) * int(arr[1][1]) - int(arr[1][0]) * int(arr[0][1])
print('|{} {}|'.format(int(arr[0][0]), int(arr[0][1])))
print('|{} {}|'.format(int(arr[1][0]), int(arr[1][1])))
print('行列式的值为：{}'.format(result))
