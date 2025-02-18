# def add(x,y):
#     return x+y
# import functools
# a=functools.reduce(add,[1,2,3,4,5])
# print(a)
# #add(add(add(add(1,2),3),4),5)

# b=functools.reduce(lambda x,y:x*y,range(1,11))
# print(b)
# #与闭包类似
# square=functools.partial(pow,exp=2)
# square(2)
# square(3)
# cube=functools.partial(pow,exp=3)
# cube(3)


import time
import functools
def time_master(func):
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
def myfunc():
    time.sleep(2)
    print('I love lianhua')
p=time_master(myfunc)
p()#调用call_func函数
print(myfunc.__name__)#装饰器的副作用
print(p.__name__)#装饰器的副作用
