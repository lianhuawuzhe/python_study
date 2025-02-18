# x=[1,2,3]
# y=x
# x[1]=1
# print(y)
# x=[1,2,3]
# y=x.copy()
# x[1]=1
# print(y)
# x=[1,2,3]
# y=x[:]
# x[1]=1
# print(y)

import copy
x=[[1,2,3],[4,5,6],[7,8,9]]
# y=x.copy()
# x[1][1]=0
# print(x)
# print(y)
y=copy.copy(x)
# x[1][1]=0
# print(x)
# print(y)
y=copy.deepcopy(x)
x[1][1]=0
print(x)
print(y)