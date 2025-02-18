# #运算符的多态
# 3+5
# 3*5
# 'py'+'lianhua'
# 'lianhua'*3

# #函数的多态
# len('lianhua')#字符个数
# len(['lianhua','py','bjfu'])
# len({'name':'lianhua','age':18})

# #类继承的多态,重写
# class shape:
#     def __init__(self,name):
#         self.name=name
#     def area(self):
#         pass

# class square(shape):
#     def __init__(self, length):
#         super().__init__('正方形')
#         self.length=length
#     def area(self):
#         return self.length*self.length

# class circlre(shape):
#     def __init__(self, radius):
#         super().__init__('圆形')
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius

# class triangle(shape):
#     def __init__(self, base,height):
#         super().__init__('三角形')
#         self.base=base
#         self.height=height
#     def area(self):
#         return self.base*self.height/2

# s=square(5)
# c=circlre(6)
# t=triangle(3,4)
# s.name
# c.name
# t.name
# s.area()
# c.area()
# t.area()


class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只猫,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('miao')

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只狗,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('wow')

class pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只猪,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('oink')

c=cat('web',4)
d=dog('fish',7)
p=pig('dada',5)

def animal(x):
    x.intro()
    x.say()

animal(c)
animal(d)

# class byc:#鸭子类型
#     def intro(self):
#         print('我曾经跨国三和大海')
#     def say(self):
#         print('都有自行车了,还要什么兰博基尼')

# b=byc()
# animal(b)