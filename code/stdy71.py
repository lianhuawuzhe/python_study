# class C:
#     def __init__(self):
#         self._x=250#隐藏使用
#     def getx(self):
#         return self._x
#     def setx(self,value):
#         self._x=value
#     def delx(self):
#         del self._x
#     x=property(getx,setx,delx)
# #     属性绑定
# # 使用 property() 函数将 getx、setx、delx 分别绑定到属性 x 的读取、写入和删除操作。
# # 此时，x 成为一个“托管属性”，所有对 x 的操作都会通过对应的方法间接操作 _x。

# c=C()
# print(c.x)
# c.x=520
# print(c.__dict__)
# del c.x
# print(c.__dict__)
# class D:
#     def __init__(self):
#         self._x=257
#     def __getattr__(self,name):
#         if name=='x':
#             return self._x
#         else:
#             super().__getattr__(name)
#     def __setattr__(self,name,value):
#         if name=='x':
#             super().__setattr__('_x',value)
#         else:
#             super().__setattr__(name,value)
#     def __delattr__(self,name):
#         if name=='x':
#             super().__delattr__('_x')
#         else:
#             super().__delattr__(name)

# d=D()
# print(d.x)
# d.x=520
# print(d.__dict__)
# del d._x
# print(d.__dict__)



# d=E()
# print(d.x)
# d.x=300
# print(d.x)


# class E:
#     def __init__(self):
#         self._x=250
#     def x(self):
#         return self._x
#     x=property(x)


# class E:
#     def __init__(self):
#         self._x=250
#     @property
#     def x(self):
#         return self._x
# e=E()
# print(e.x)
# e.x=520

# class E:
#     def __init__(self):
#         self._x=250
#     def x(self):
#         return self._x
#     x=property(x)

class D:
    def __init__(self):
        self._x=250
    def __getattr__(self,name):
        if name=='x':
            return self._x
        else:
            super().__getattr__(name)
    def __setattr__(self,name,value):
        if name=='x':
            super().__setattr__('_x',value)
        else:
            super().__setattr__(name,value)
    def __delattr__(self,name):
        if name=='x':
            del self._x
        else:
            super().__delattr__(name)

d=D()
print(d.x)
d.x=520
print(d.__dict__)
del d._x
print(d.__dict__)


# class E:
#     def __init__(self):
#         self._x=250
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self,value):
#         self._x=value
#         #在这个过程中，
#         #self._x 被直接赋值为 value，
#         # 而没有通过 x 的 setter 方法进行赋值，
#         # 因此不会导致递归调用。
#     @x.deleter
#     def x(self):
#         del self._x
# e=E()
# print(e.x)
# e.x=520
# print(e.__dict__)
# del e.x
# print(e.__dict__)


# class E:
#     def __init__(self):
#         self._x=250
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self,value):
#         self._x=value
#     @x.deleter
#     def x(self):
#         del self._x
# e=E()
# print(e.x)
# e.x=520
# print(e.__dict__)
# del e.x
# print(e.__dict__)