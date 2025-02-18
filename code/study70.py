# #__call_-(self[,args])
# class C:
#     def __call__(self,*args,**kwargs):
#         print(f'位置参数{args}\n关键字参数{kwargs}')
# c=C()
# c(1,2,3,x=4,y=5)


# class power:
#     def __init__(self,exp):
#         self.exp=exp
#     def __call__(self,base):
#         return base**self.exp
# square=power(2)
# cube=power(3)
# print(square(3))
# print(cube(4))


# #__str__(self) __repr__(self)
# #str给人看的   repr给机器就看的
# str(520)#520
# repr(520)#520
# str('lianhua')#'lianhua'
# repr('lianhua')#'"lianhua"'多义词引号
# #eval去引号后执行，相当于repr的反函数
# eval(str('lianhua'))#报错
# eval(repr('lianhua'))#lianhua
# eval(repr(520))#520


# #repr可以代仓str
# class C:
#     def __repr__(self):
#         return 'I love lainhua'
# c=C()
# print(str(c))
# print(repr(c))#repr(c)得到<__main__

# #str只用于对象出现在打印操作的顶层
# #repr场景更多
# cs=[C(),C(),C()]
# for each in cs:
#     print(each)
# print(cs)
#换成str

# class C:
#     def __str__(self):
#         return 'I love lainhua'
# c=C()
# print(str(c))
# print(repr(c))#repr(c)得到<__main__

# #str只用于对象出现在打印操作的顶层
# #repr场景更多
# cs=[C(),C(),C()]
# for each in cs:
#     print(each)
# print(cs)


#同时定义str和repr得到不同显示
#repr可以代仓str

class C:
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return f'data={self.data}'
    def __repr__(self):
        return f'C{self.data}'
    def __add__(self,other):
        self.data+=other

c=C(250)
print(c)#data=250
c#C(250)
c+250
print(c)#data=500
c#C(500)
print(C(39))#data=39