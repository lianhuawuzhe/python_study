# class C:
#     def funa(self):
#         print(self)
#     @classmethod
#     def funb(cls):
#         print(cls)
# c=C()
# c.funa()#绑定对象
# c.funb()#绑定C
# class C:
#     count=0
#     def __init__(self):
#         C.count+=1
#     @classmethod
#     def getc(cls):
#         print(f'该类一共实例化了{cls.count}个实例对象')
# c1=C()
# c2=C()
# c3=C()
# c3.getc()
# c3.count=1
# #一般来说，实例属性和类属性同名时，实例属性会覆盖类属性
# #但是这里是类方法，影响不大
# print(c3.count)
# c3.getc()

# class C:
#     @staticmethod
#     def func():
#         print('i love lianhua')
# c=C()
# c.func()
# C.func()


# class C:
#     count=0
#     def __init__(self):
#         C.count+=1
#     @staticmethod
#     def getc():
#         print(f'该类一共实力化了{C.count}个对象')#拿不到类直接.C
# c1=C()
# c2=C()
# c3=C()
# c3.getc()

# class C:
#     count=0
#     @classmethod
#     def add(cls):
#         cls.count+=1
#     def __init__(self):
#         self.add()
#     @classmethod
#     def getc(cls):
#         print(f'该类一共实例化了{cls.count}个实例对象')
# class D(C):
#     count=0
# class E(C):
#     count=0
# c1=C()
# d1,d2=D(),D()
# e1,e2,e3=E(),E(),E()
# c1.getc()
# d1.getc()
# e1.getc()