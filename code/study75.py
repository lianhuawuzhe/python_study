# class C:
#     def func(self,x):
#         return x
# c=C()
# C.func#函数
# c.fun#方法


# class C:
#     @classmethod
#     def __doc__(cls):
#         return f'I love fishc from class {cls.__name__}'
# c=C()
# print(c.__doc__())
# print(C.__doc__())

# class D:
#     @classmethod
#     @property
#     def __doc__(cls):
#         return  f'i love fishc from class {cls.__name__}'
# d=D()
# d.__doc__
# D.__doc__

class methodtype:
    def __init__(self,func,obj):
        self.__func__=func
        self.__self__=obj
    def __call__(self,*args,**kwargs):
        func=self.__func__
        obj=self.__self__
        print('小白')
        return func(obj,*args,**kwargs)
class Classnethond:
    def __init__(self,f):
        self.f=f
    def __get__(self,obj,cls=None):
        if cls is None:
            print('旺财')
            cls=type(obj)
        if hasattr(type(self.f),'__get__'):
            print(f'来福，type(self.f)->{type(self.f)}')
            return self.f.__get__(cls,cls)
        return methodtype(self.f,cls)
class D:
    @Classnethond
    @property
    def __doc__(cls):
        return f'i love fishc from class {cls.__name__}'
d=D()
d.__doc__