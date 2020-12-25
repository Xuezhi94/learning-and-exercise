#用第一种多项式表示法来设计Python程序，并进行两个多项式a(x)=3x^4+7x^3+6x+2和b(x)=x^4+5x^3+2x^2+9
poly_items=6   #首项存储多项式次数，其余项依次数从高到低存储各项系数
def poly_print(poly,items):
    max_exp=poly[0]
    for i in range(1,poly[0]+2):
        max_exp -=1
        if poly[i]:
            if max_exp+1:
                print('%dX^%d'%(poly[i],max_exp+1),end=' ')
            else:
                print('%d'%poly[i])
            if max_exp>=0:
                print('+',end=' ')
def poly_sum(poly1,poly2):
    #计算并打印两多项式之和
    result=[None]*poly_items
    result[0]=poly1[0]
    for i in range(1,result[0]+2):
        result[i]=poly1[i]+poly2[i]
    poly_print(result,poly_print)

poly_a=[4,3,7,0,6,2]  #声明多项式a
poly_b=[4,1,5,2,0,9]  #声明多项式b
print('多项式a=',end=' ')
poly_print(poly_a,poly_items)
print('多项式b=',end=' ')
poly_print(poly_b,poly_items)
print('a+b=',end=' ')
poly_sum(poly_a,poly_b)

