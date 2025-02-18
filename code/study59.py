# class C:
#     def get_self(self):
#         print(self)
# d=C()
# c=C()
# d.x=250
# c.x=520
# c.x#520
# d.x#250
# c.y=660
# #内省
# c.__dict__#{'x':520,'y':660}

# class C:
#     def set_x(self,v):
#         self.x=v

# c=C()
# c.__dict__#{}
# c.set_x(250)
# c.__dict__#{'x':250}

# class C:
#     x=100
#     def set_x(self,v):
#         x=v
# c=C()
# c.set_x(250)#谁都改不了
# c.x#100
# C.x#100
# C.x=250
# c.x#250
# c.__dict__#{}对象没有不代表类没有。类没有不代表父类没有

# class C:
#     x=100
#     def set_x(self,v):
#         x=

class C:
    pass
#当字典使用
C.x=250
C.z=[1,2,3]
C.y='lianhua'
print(C.x)
print(C.z)
print(C.y)

#真正的字典
d={}
d['x']=250
d['y']='lianhua'
d['z']=[1,2,3]
print(d['x'])
print(d['y'])
print(d['z'])

#更常用的方式
class C:
     pass
c=C()
c.x=250
c.y='小甲鱼'
c.z=[1,2,3]