# #__init__()
# class C:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         return self.x+self.y
#     def mul(self):
#         return self.x*self.y
# c=C(2,3)
# c.add()#5
# c.mul()#6
# print(c.__dict__)

# #子类对父类的重写
# class D(C):
#     def __init__(self, x, y,z):
#         C.__init__(self,x,y)
#         self.z=z
#     def add(self):
#         return C.add(self)+self.z
#     def mul(self):
#         return C.mul(self)*self.z
# d=D(2,3,4)
# print(d.add())
# print(d.mul())
# #调用未绑定的父类的方法：直接通过类访问类里方法的做法

class A:
    def __init__(self):
        print('hellp, 我是A')
class B1(A):
    def __init__(self):
        super().__init__()
        print('hello,我是B1')
class B2(A):
    def __init__(self):
        super().__init__()
        print('hello,我是B2')
class C(B1,B2):
    def __init__(self):
        super().__init__()
        print('hello，我是C')
c=C()

#查找类的MRO
#1.
C.mro()
B1.mro()
#2.
C.__mro__
B1.__mro__

