#普通函数
def squarex(x):
    return x*x
squarex(3)#函数的引用squarex

#lambda
squarey=lambda y:y*y#函数引用squarey
squarey(3)

#但是，lambda是一个表达式
y=[lambda x:x*x,2,3]
y[0](y[1])#4
y[0](y[2])#9

mapped=map(lambda x:ord(x)+10,'lianhua')
list(mapped)

def boring(x):
    return ord(x)+10
list(map(boring,'lianhua'))

list(filter(lambda x:x%2,range(10)))
