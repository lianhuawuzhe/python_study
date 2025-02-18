# #__contains__(self)

# class C:
#     def __init__(self,data):
#         self.data=data
#     def __contains__(self,item):
#         print('hi')
#         return item in self.data
# c=C([1,2,3,4,5])
# print(3 in c)

#__contains__(self)

# class C:
#     def __init__(self,data):
#         self.data=data
#     def __iter__(self):
#         print('iter',end='->')
#         self.i=0
#         return self
#     def __next__(self):
#         print('next',end='->')
#         if self.i==len(self.data):
#             raise StopIteration
#         item=self.data[self.i]
#         self.i+=1
#         return item

# c=C([1,2,3,4,5])
# print(3 in c)
# print(6 in c)


# class C:
#     def __init__(self,data):
#         self.data=data
#     def __getitem__(self,index):
#         print('getitem',end='->')
#         return self.data[index]

# c=C([1,2,3,4,5])
# print(3 in c)
# print(6 in c)


# class D:
#     def __bool__(self):
#         print('bool')
#         return True
# d=D()
# print(bool(d))

# class D:
#     def __init__(self,data):
#         self.data=data
#     def __len__(self):
#         print('len')
#         return len(self.data)#Ture为非零
# d=D('lianhua')
# print(bool(d))


# class S(str):
#     def __lt__(self,other):
#         return len(self)<len(other)
#     def __gt__(self,other):
#         return len(self)>len(other)
#     def __eq__(self,other):
#         return len(self)==len(other)
#     __le__=None#这里不加这个的话，还是比较编码，加了出现不合适的关系会报错
#     __ge__=None
#     __ne__=None

# s=S('lianhua')
# p=S('Lianhua')
# print(s==p)

class C:
    def __init__(self,data):
        self.data=data
    def __iter__(self):
        print('iter',end='->')
        self.i=0
        return self
    def __next__(self):
        print('next',end='->')
        if self.i==len(self.data):
            raise StopIteration
        item=self.data[self.i]
        self.i+=1
        return item
    __contains__=None

c=C([1,2,3,4,5])
print(3 in c)

