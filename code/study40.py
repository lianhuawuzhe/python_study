def myfunc():
    pass#空语句，占位符
myfunc()
def myfunc():
    for i in range(3):
        print('I love lianhua')
myfunc()
def myfunc(name,times):#形参
    for i in range(times):
        print(f'I love {name}.')
myfunc('python',5)#实参
def div(x,y):
    if y==0:
        return '除数不能为0'
    else:
        return x/y#执行return后马上退出
div(4,2)

def myfunc():
    pass
print(myfunc())