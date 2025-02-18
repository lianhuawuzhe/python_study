# #加法

# class S(str):
#     def __add__(self,other):
#         return len(self)+len(other)
# s1=S('lianhua')
# s2=S('python')
# print(s1+s2)#s1+s2即s1.__add__(s2)
# print(s1+'python')
# print('python'+s2)


# #反算术运算加法
# class s1(str):
#     def __add__(self,other):
#         return NotImplemented#表示魔法方法未实现
# #p1必须不能实现add,不然优先用左侧
# class s2(str):
#     def __radd__(self,other):
#         #不能写成add，矛盾
#         return len(self)+len(other)
# p1=s1('banaba')
# p2=s2('apple')
# print(p1+p2)

# #增强赋值运算,运算加赋值
# #p1+=p2即p1=p1.__iadd__(s2),会修改对象自身
# class s1(str):
#     def __iadd__(self,other):
#         return len(self)+len(other)

# class s2(str):
#     def __radd__(self,other):
#         return len(self)+len(other)
# p1=s1('apple')
# p2=s2('banana')
# p1+=p2
# print(p1)
# print(type(p1))#class被改为int


# #如果增强运算符没实现左侧的魔法方法，则使用add 或者 radd
# p2+=p2 #p2 p2同类，去str查找add
# print(p2)
# print(type(p2))


# #int（self）拦截魔法方法,只要一个参数
# #将中文转化成整数
# class myint:
#     def __init__(self,num):
#         self.num=num
    
#     def __int__(self):
#         try:
#             return int(self.num)
#         except ValueError:
#             zh={'零':0,'一':1,'二':2,'三':3,'四':4,
#             '五':5,'六':6,'七':7,'八':8,'九':9}
#             result=0
#         for each in self.num:
#             if each in zh:
#                 result+=zh[each]
#             else:
#                 result+=int(each)
#             result*=10

#         return result//10
# n=myint('五二零1413')
# print(n)#print(n) 打印的是 n 这个对象本身，而不是它的整数值

# #在 Python 中，当你打印一个对象（像 n 这样的自定义类对象）时，
# # 默认情况下，它不会直接显示对象的内容，而是显示它的内存地址，
# # 比如 <__main__.myint object at 0x...>。
# # 如果你想让打印出来的内容更有意义（比如数字），
# # 你需要告诉 Python 如何显示这个对象的内容
# print(int(n))


# print(int(3.14))


