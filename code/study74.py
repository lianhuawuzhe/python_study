# class D:
#     def __get__(self,instance,owner):
#         print('get')
#     def __set__(self,instance,value):
#         print('set')

# class C:
#     x=D()
#     def __getattribute__(self, name):
#         print('aha')
# c=C()
# c.x



# c.x='fish'
# c.x
# print(c.__dict__)
# c.__dict__['x']='fishc'
# print(c.__dict__)
# c.x

class D:
    def __set_name__(self,owner,name):
        self.name=name
    def __get__(self,instance,owner):
        print('get')
        return instance.__dict__.get(self.name)
    def __set__(self,instance,value):
        print('set')
        instance.__dict__[self.name]=value
class C:
    x=D()
c=C()
c.x
print(c.__dict__)
c.x=250
print(c.__dict__)
print(c.x)


