# def funa():
#     print('lianhua')
# def funb():
#     funa()
# def func():
#     print('lianhua')
#     func()
# func()
# def func(i):
#     if i>0:
#         print('lianhua')
#         i-=1
#         func(i)
# func(3)


###阶乘
#迭代
# def fac(n):
#     res=1
#     for i in range(1,n+1):
#         res=i*res
#     return res
# n=int(input('请输入一个数：'))
# p=fac(n)
# print(f'{n}的阶乘是{p}')

# #递归
# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# n=int(input('请输入一个数：'))
# p=fac(n)
# print(f'{n}的阶乘是{p}')

###斐波那契数列
#迭代
def fac(n):
    a=1
    b=1
    c=1
    while n>2:
        c=a+b
        a=b
        b=c
        n-=1
    return c
fac(12)

#递归
def fac(n):
    if n==1 or n==2:
        return 1
    else:
        return fac(n-1)+fac(n-2)
print(fac(12))
        
