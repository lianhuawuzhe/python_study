#函数
# class C:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

# c=C('lianhua',18)
# print(hasattr(c,'name'))
# print(getattr(c,'name'))
# print(getattr(c,'_C__age'))
# print(setattr(c,'_C__age',19))
# print(getattr(c,'_C__age'))
# delattr(c,'_C__age')
# print(hasattr(c,'_C__age_'))


# class C:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def __getattribute__(self, attrname):
#         print('拿来吧你')
#         return super().__getattribute__(attrname)
#         #在方法内部，首先打印 '拿来吧你'，
#         # 然后使用 super().__getattribute__(attrname) 调用父类的 __getattribute__ 方法，
#         # 获取属性的实际值。
#     def __getattr__(self,attrname):#当用户试图获取不存在的属性触发
#         if attrname=='lianhua':
#             print(' i love lianhua')
#         else:
#             raise ArithmeticError(attrname)
# c=C('lianhua',18)
# print(getattr(c,'name'))
# print(c.x)


# #无限递归
# class D:
#     def __setattr__(self, name, value):
#         self.name=value
# #在您提供的代码中，
# # 类 D 定义了 __setattr__ 方法，
# # 用于拦截对实例属性的赋值操作。 
# # 当您创建 D 类的实例 d 并尝试设置 d.name = 'lianhua' 时，
# # __setattr__ 方法会被调用。
# #  然而，在 __setattr__ 方法内部，
# # 您直接使用 self.name = value 来设置属性值，
# # 这会再次触发 __setattr__ 方法，导致无限递归调用，
# # 最终引发 RecursionError。
# d=D()
# d.name='lianhua'




# class D:
#     def __setattr__(self, name, value):
#         self.__dict__[name]=value
# d=D()
# d.name='lianhua'


class D:
    def __setattr__(self, name, value):
        self.__dict__[name]=value
    def __delattr__(self, name):
        del self.__dict__[name]
d=D()
d.name='lianhua'
print(d.__dict__)
del d.name
print(d.__dict__)


