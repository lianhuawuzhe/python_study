# print(int)
# type('lainua') is str#返回对象对应的类，True
# type([])('lainhua')
# type({}).fromkeys('python')

# class C:
#     def __init__(self,x):
#         self.x=x
# c=C(520)
# d=type(c)(520)
# print(c.__class__)
# print(d.__class__)
# type(C)#type,类也是type生成的对象
# type(type)#type
# class C:
#     pass
# C=type('C',(),{})#名字，父类默认object,函数和属性
# c=C()
# c.__class__
# C.__bases__
# D=type('D',(C,),{})
# D.__bases__
# E=type('E',(),dict(x=250,y=520))
# E.x
# E.y

# def func(self,name='lainhua'):#因为是类，所以要self
#     print(f'hello {name}')
# F=type('F',(),dict(sayhi=func))
# f=F()
# f.sayhi()
# f.sayhi('py')


# #__init_subclass__()
# class C:
#     def __init_subclass__(cls):
#         print('父爱如山')
#         cls.x=520
# class D(C):
#     x=250
# print(D.x)

# class C:
#     def __init_subclass__(cls,value):
#         print('父爱如山')
#         cls.x=value
# class D(C,value=520):
#     x=250
# print(D.x)


class C:
    def __init_subclass__(cls,value1,value2):
        print('父爱如山')
        cls.x=value1
        cls.y=value2
D=type('D',(C,),dict(x=250),value1=520,value2=666)
print(D.x)
print(D.y)




