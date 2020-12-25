#斐波那契数列的递推公式：fib(n)=fib(n-1)+fib(n-2) if n>=3; fib(1)=fib(2)=1
def fab(n):
    if n <= 0:
        print('输入错误！')
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


n = int(input('请输入一个正整数：'))
result = fab(n)
if result != -1:
    print('fab(%d) = %d' % (n, result))
