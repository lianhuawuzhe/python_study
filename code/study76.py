# def report(cls):
#     def oncall(*args,**kwargs):#args=(1,2,3)
#         print('我要开始实例化对象了')
#         _=cls(*args,**kwargs)#解包
#         print('实例化已经完成')
#         return _
#     return oncall
# @report#C=report(C)
# class C:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#         print('构造函数被调用了')
# c=C(1,2,3)#oncall(1,2,3)


# class counter:
#     def __init__(self,func):
#         self.count=0
#         self.func=func

#     def __call__(self,*args,**kwargs):
#         self.count+=1
#         print(f'已经被调用了{self.count}次')
#         return self.func(*args,**kwargs)
# @counter#sayhi=counter(sayhi),sayji已经变成counter的一个实例化对象

# def sayhi():
#     print('hi')
# sayhi()#对象当成函数用，会调用call
# sayhi()
# sayhi()


def report(cls):
    class check:
        def __init__(self, *args,**kwargs):
             self.obj=cls(*args,**kwargs)

        def __getattr__(self,name):
            print(f'正在访问{name}')
            return getattr(self.obj,name)
    return check
@report#C=report(C)
class C:#被替换为class check
    def __init__(self,name):
        self.name=name
    def sayhi(self):
        print(f'hi {self.name}')
    def sayhey(self):
        print(f'hey {self.name}')

c1=C('c1')#实例化2次
c2=C('c2')
c1.name
c2.name
c1.sayhi()
c2.sayhey()

# class check:
#     def __init__(self, cls):
#         self.cls=cls
#     def __call__(self,*args,**kwargs):
#         self.obj=cls(*args,**kwargs)
#         return self
#     def __getattr__(self,name):
#         print(f'正在访问{name}')
#         return getattr(self.obj,name)
# @check#C=check(C)，产生对象,实例化一次
# class C:
#     def __init__(self,name):
#         self.name=name
#     def sayhi(self):
#         print(f'hi {self.name}')
#     def sayhey(self):
#         print(f'hey {self.name}')

# c1=C('c1')#c1,c2均是check类对象，c1c2访问2次call
# c2=C('c2')#self.obj,c1被c2覆盖
# c1.name
# c2.name
# c1.sayhi()
# c2.sayhey()