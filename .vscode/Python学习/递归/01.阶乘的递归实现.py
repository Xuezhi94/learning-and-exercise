#计算给定非负整数的阶乘
#递推公式：fractorial(n)=1 if n=0; =n*fractorial(n-1) if n>=1
def fractorial(n):
    if n < 0:
        print('error! the number should be nonnegtive!')
        return -1
    if n == 0:
        return 1
    else:
        return n * fractorial(n - 1)


num = int(input('请输入一个整数：'))
result = fractorial(num)
print('%d的阶乘为:%d' % (num, result))
