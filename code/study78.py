# class Metac(type):
#     pass
# class C(metaclass=Metac):
#     pass
# c=C()
# print(type(c))
# print(type(C))
# print(type(Metac))

# class metac(type):
#     def __new__(mcls,name,bases,attrs):
#         print('new in metac')
#         return type.__new__(mcls,name,bases,attrs)
#     def __init__(cls,name,bases,attrs):
#         print('init in metac')
#         type.__init__(cls,name,bases,attrs)
# class C(metaclass=metac):
#     def __new__(cls):
#         print('new in C')
#         return super().__new__(cls)#object
#     def __init__(self):
#         print('init in C')
# c=C()


# class metac(type):
#     def __new__(mcls,name,bases,attrs):
#         print('new in metac')
#         print(f'mcls={mcls},name={name},bases={bases},sttrs={attrs}')
#         return type.__new__(mcls,name,bases,attrs)
#     def __init__(cls,name,bases,attrs):
#         print('init in metac')
#         print(f'cls={cls},name={name},bases={bases},sttrs={attrs}')

#         type.__init__(cls,name,bases,attrs)
# class C(metaclass=metac):
#     def __new__(cls):
#         print('new in C')
#         return super().__new__(cls)#object
#     def __init__(self):
#         print('init in C')
# c=C()


class metac(type):
    def __call__(cls,*args,**kwargs):
        print('call in metac')
class C(metaclass=metac):
    pass
c=C()    