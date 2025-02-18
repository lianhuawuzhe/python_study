# class C:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self, *args, **kwds):
#         print('call in C')
#     def func(self):
#         print(self.name*2)
# c=C('lianhua')
# c.func()

# class metac(type):
#     def __new__(mcls,name,bases,attrs):
#         attrs['author']='lianhua'
#         return type.__new__(mcls,name,bases,attrs)
# class C(metaclass=metac):
#     pass
# class D(metaclass=metac):
#     pass
# c=C()
# d=D()
# print(c.author)
# print(c.author)
# class metac(type):
#     def __init__(cls,name,bases,attrs):
#         cls.author='lianhua'
#         return type.__init__(cls,name,bases,attrs)
# class C(metaclass=metac):
#     pass
# class D(metaclass=metac):
#     pass
# c=C()
# d=D()
# print(c.author)
# print(c.author)

# class metac(type):
#     def __init__(cls,name,bases,attrs):
#         if not name.istitle():
#             raise TypeError('类名必须是大写字母开头')
#         type.__init__(cls,name,bases,attrs)
# class d(metaclass=metac):
#     pass

# class metac(type):
#     def __call__(cls,*args,**kwargs):
#         new_args=[each.upper() for  each in args if isinstance(each,str)]
#         return type.__call__(cls,*new_args,**kwargs)
# class C(metaclass=metac):
#     def __init__(self,name):
#         self.name=name
# c=C('LianHua')
# print(c.name)



# class metac(type):
#     def __call__(cls,*args,**kwargs):
#         if args:
#             raise TypeError('仅支持关键字对象')
#         return type.__call__(cls,*args,**kwargs)
# class C(metaclass=metac):
#     def __init__(self,name):
#         self.name=name
# c=C('name=lianhua')
# print(c.name)


# class noinstance(type):
#     def __call__(self, *args, **kwds):
#         raise TypeError('该类不支持实例化')
# class C(metaclass=noinstance):
#     @staticmethod
#     def ok():
#         print('静态直接访问是被允许的')
#     @classmethod
#     def ok1(cls):
#         print('类方法直接访问是被允许的')
# C.ok()
# C.ok1()


class noinstance(type):
    def __init__(cls, *args, **kwargs):
        cls.a=None
        type.__init__(cls,*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a=type.__call__(cls,*args,**kwargs)
            return cls.a
        else:
            return cls.a
class C(metaclass=noinstance):
    pass

c1=C()
c2=C()
print(c1 is c2)