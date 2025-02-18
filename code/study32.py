# print([1,2,3]+[4,5,6,7])
# print((1,2,3)+(4,5,6))
# print((1,2,3)*3)
# print('123'+'456')
# s=[1,2,3]
# print(id(s))
# print(s*2)
# print(id(s))
# t=(1,2,3)
# print(id(t))
# t*=2
# print(id(t))
# x='fishc'
# y='fishc'
# print(x is y)
# print('lian' in 'lianhua')
# x='fishc'
# y=[1,2]
# del x,y
# print(x)
# print(y)
# x=[1,2,3,4,5]
# del x[1:4]
# print(x)
# y=[1,2,3,4,5]
# y[1:4]=[]
# print(y)
# x=[1,2,3,4,5]
# del x[::2]
# print(x)

x=[1,2,3,4,5]
x.clear()
print(x)
y=[1,2,3,4,5]
del y[::]
print(y)