
# class B(A):#子类
#     pass
# b=B()
# b.x
# b.hello()
# class B(A):
#     x=990#覆盖
#     def hello(self):#覆盖
#         print('你好，我是B')
# b=B()
# b.x
# b.hello()

# #判断一个对象是否属于某个类
# isinstance(b,B)
# isinstance(b,A)
# #检测一个类是否为另一个类的子类
# issubclass(A,B)
# issubclass(B,A)
# class A:
#     x=520
#     def hello(self):
#         print('hello,我是A')

# class B:
#     x=880
#     y=250
#     def hello(self):
#         print('你好，我是C')
# #多重继承
# class C(A,B):
#     pass
# c=C()
# c.x#520
# c.hello()#A
# #从左到右访问
# c.y#250

# class Turtle:
#     def say(self):
#         print('不积跬步无以至千里')
# class Cat:
#     def say(self):
#         print('瞄')
# class Dog:
#     def say(self):
#         print('汪汪汪')
# class Garden:
#     t=Turtle()
#     c=Cat()
#     d=Dog()
#     def say(self):
#         self.t.say()#加上self
#         self.c.say()
#         self.d.say()
# g=Garden()
# g.say()
