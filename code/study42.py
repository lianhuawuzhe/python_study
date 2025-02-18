# print('lianhua')
# print('lianhua','爱','python')
# def myfunc(*args):
#     print('有{}个参数'.format(len(args)))
#     print('第二个参数是：{}'.format(args[1]))
#     print(args)#元组有打包和解包的能力
# myfunc('lianhua','python',1,2,3)
# def myfunc():
#     return 1,2,3
# print(myfunc())
# x,y,z=myfunc()
# print(x)
# print(y)
# print(z)
# #函数参数通过星号实现打包操作，实际是元组

# def myfunc(*args,a,b):#收集参数后面必须使用关键字参数
#     print(args,a,b)
# myfunc(1,2,3,a=4,b=5)

# def abc(a,*,b,c):#*为匿名的收集参数
#     print(a,b,c)
# abc(1,b=2,c=3)

# def myfunc(**kwargs):#把参数打包成字典
#     print(kwargs)
# myfunc(a=1,b=2,c=3)

# #混合使用
# def myfunc(a,*b,**c):
#     print(a,b,c)
# myfunc(1,2,3,4,x=5,y=6)


# #同时用一个和两个*
# print(help(str.format))


args=(1,2,3,4)
def myfunc(a,b,c,d):
    print(a,b,c,d)
print(myfunc(*args))#解包

kwargs={'a':1,'b':2,'c':3,'d':4}
print(myfunc(**kwargs))#关键字参数