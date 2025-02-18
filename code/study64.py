# #__init__
# #对象诞生先调用__new__(cls[,…])创建类的实例，返回对象self,再传递给__init__()
# class caps(str):
#     def __new__(cls,string):
#         string=string.upper()
#         return super().__new__(cls,string)# 调用父类 str 的 __new__ 方法创建字符串实例



# cs=caps('Fishc')
# print(cs)
# print(cs.lower())#继承str
# print(cs.capitalize())

#__del__(self)
# class C:
#     def __init__(self):
#         print('我来了')
#     def __del__(self):
#         print('我走了')

# c=C()
# del c#对象被销毁才会调用魔法方法

# c=C()
# d=c#引用,被引用不会被销毁
# del c
# del d


#利用全局变量
# class D:
#     def __init__(self,name):
#         self.name=name
#     def __del__(self):
#         global x
#         x=self

# d=D('小甲鱼')
# print(d.name)
# del d#对象销毁之前最后一次拦截对象
# print(x)
# print(x.name)

#函数调用
class E:
    def __init__(self,name,func):
        self.name=name
        self.func=func
    def __del__(self):
        self.func(self)

#闭包
def outter():
    x=0
    def inner(y=None):
        nonlocal x#用于在嵌套函数中声明变量为外层函数的局部变量，使得内层函数可以修改外层函数的变量。 

        if y:
            x=y
        else:
            return x#窃取self
    return inner

f=outter()#调用 outter，返回 inner 函数，并将其赋值给变量 f。此时，f 是一个闭包，封闭了 outter 中的变量 x。
e=E('lianhua',f)
print(e)
e.name
del e
g=f()#就是e
print(g.name)

