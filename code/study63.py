# class C:
#     def __init__(self,x):
#         self.__x=x
#     def set_x(self,x):
#         self.__x=x
#     def get_x(self):
#         print(self.__x)
# c=C(250)
# #c.__x访问不到
# c.get_x()
# c.set_x(520)
# c.get_x()
# print(c.__dict__)
# print(c._C__x)#私有变量实际是改了个名字



# #方法名
# class D:
#     def __func(self):
#         print('fishc')

# d=D()
# #d.__func()
# d._D__func()
# #添加私有变量？不行
# #名字改编是发生在类实例化对象时
# c.__y=250


#  _变量仅供内部访问，不要去访问
# 变量_


# class C:
#     def __init__(self,x):
#         self.x=x
# c=C(250)
# print(c.__dict__)
# c.y=520
# print(c.__dict__)
# c.__dict__['z']=666
# print(c.__dict__)




class C:
    __slots__=['x','y']
    def __init__(self,x):
        self.x=x


c=C(250)
c.y=520
print(c.__dict__)

# class D:
#     __slots__=['x','y']
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

# d=D(3,4,5)

# class C:
#     __slots__=['x','y']
#     def __init__(self,x):
#         self.x=x

# class E(C):
#     pass
# e=E(520)
# e.y=250
# e.z=666
# print('e.__slots__')#有属性，但不生效
# print(e.__dict__)