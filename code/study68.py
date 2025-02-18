# class C:
#     def __getitem__(self,index):
#         print(index)
# c=C()
# c[2]#2
# c[2:8]#slice(2,8,None),bif函数，切片是它的语法糖
# s='I love fishc'
# s[2:6]#'love
# s[slice(2,6)]#'love
# s[7:]#'fishc
# s[slice(7,None)]#'fishc
# s[::4]#'Ivi
# s[slice(None,None,4)]




#为索引或切片赋值会被__setitem__()拦截
# class D:
#     def __init__(self,data):
#         self.data=data
#     def __getitem__(self,index):
#         return self.data[index]
#     def __setitem__(self,index,value):
#         self.data[index]=value 
# d = D([1, 2, 3,4,5])
# print(d[0])  # 输出 1（调用 __getitem__）
# d[1] = 1
# print(d.data)  
# d[2:4]=[2,3]
# d[:]#[1,1,2,3,5]

# #与获取相关的操作也会被拦截
# class D:
#     def __init__(self,data):
#         self.data=data
#     def __getitem__(self,index):
#         return self.data[index]*2
# d=D([1,2,3,4,5])
# for i in d:
#     print(i,end=' ')


#__iter__(self)  __next__(self)
#模拟for的执行流程
x=[1,1,2,3,5]
_=iter(x)
while True:
    try:
        #i=_.__next__()
        i=next(_)#这样也成功了
    except StopIteration:
        break
    print(i,end=' ')



# #自己创建迭代器对象
# class double:
#     def __init__(self,start,stop):
#         self.value=start-1
#         self.stop=stop
#     def __iter__(self):
#         return self# 关键：返回自身，说明实例是迭代器
#     def __next__(self):
#         if self.value==self.stop:
#             raise StopIteration
#         self.value+=1
#         return self.value*2
# d=double(1,5)
# for i in d:
#     print(i,end=' ')



