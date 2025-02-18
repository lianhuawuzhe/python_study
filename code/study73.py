# class D:
#     def __get__(self,instance,owner):#x,D()   c    C
#         print(f'get\nself->{self}\nintstance->{instance}\nowner->{owner}')
#     def __set__(self,instance,value):
#         print(f'set\nself->{self}\nintstance->{instance}\nvalue->{value}')
#     def __delete__(self,instance):
#         print(f'delete\nself->{self}\ninstance->{instance}')
# class C:
#     x=D()
# c=C()
# c.x=250
# c.x
# del c.x
# class D:
#     def __get__(self,instance,owner):
#         return instance._x
#     def __set__(self,instance,value):
#         instance._x=value
#     def __delete__(self,instance):
#         del instance._x
# class C:
#     def __init__(self,x=250):
#         self._x=x
#     x=D()

# c=C()
# print(c.x)
# c.x=520
# print(c.__dict__)
# del c.x
# print(c.__dict__)

# class myproperty():
#     def __init__(self,fget=None,fset=None,fdel=None):
#         self.fget=fget
#         self.fset=fset
#         self.fdel=fdel
#     def __get__(self,instance,owner):
#         return self.fget(instance)#c
#     def __set__(self,instance,value):
#         self.fset(instance,value)
#     def __delete__(self,instance):
#         self.fdel(instance)

# class C:
#     def __init__(self):
#         self._x=250
#     def getx(self):
#         return self._x
#     def setx(self,value):
#         self._x=value
#     def delx(self):
#         del self._x
#     x=myproperty(getx,setx,delx)
# c=C()
# print(c.x)
# c.x=520
# print(c.__dict__)
# del c.x
# print(c.__dict__)

class myproperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)#c
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)
    def getter(self,func):
        self.fget=func
        return self
    def setter(self,func):
        self.fset=func
        return self
    def deleter(self,func):
        self.fdel=func
        return self
class E:
    def __init__(self):
        self._x=250
    x=myproperty()
    @x.getter
    def getx(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @x.deleter
    def x(self):
        del self._x

# class D:
#     def __init__(self):
#         self._x=520
#     @myproperty
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self,value):
#         self._x=value
#     @x.deleter
#     def x(self):
#         del self._x
# d=D()
# print(d.x)
# d.x=520
# print(d.__dict__)
# del d.x
# print(d.__dict__)

e=E()
print(e.x)
e.x=520
print(e.__dict__)
del e.x
print(e.__dict__)

