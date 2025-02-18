# def counter():#此时counter（）是一个生成器,每次调用提供一个数据
#     i=0
#     while i<=5:
#         yield i#每次执行生成一个数据，暂停保留状态
#         i+=1#下次调用从这里开始执行
# #使用
# for i in counter():
#     print(i)

# c=counter()
# next(c)#0
# next(c)#1
# next(c)#2
# next(c)#3
# next(c)#4
# next(c)#5
# next(c)#报错

# ###求斐波那契数列
# def fib():
#     back1,back2=0,1
#     while True:
#         yield back1
#         back1,back2=back2,back2+back1
# f=fib()
# next(f)
# next(f)
# next(f)
# next(f)
# next(f)
# next(f)
# next(f)


t=(i**2 for i in range(10))
next(t)
next(t)
next(t)
next(t)
for i in t:
    print(i)
