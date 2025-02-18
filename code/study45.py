# def myfunc():
#     print('正在调用myfunc')
# def report(func):
#     print('主人，我要开始调用函数了')
#     func()
#     print("主人，我调用完函数了")
# report(myfunc)



###时间管理大师函数
# import time
# def time_master(func):
#     print('开始运行')
#     start=time.time()#获取时间戳
#     func()
#     stop=time.time()
#     print('运行结束')
#     print(f'一共耗费{(stop-start):.2f}秒')
# def myfunc():
#     time.sleep(2)
#     print('hello lianhua')
# time_master(myfunc)

# import time
# def time_master(func):
#     def call_func():
#         print('开始运行')
#         start=time.time()
#         func()
#         stop=time.time()
#         print('运行结束')
#         print(f'一共耗费{(stop-start):.2f}秒')
#     return call_func
# @time_master
# def myfunc():
#     time.sleep(2)
#     print('I love lianhua')

# #装饰器原本的样子
# myfunc=time_master(myfunc)
# myfunc()

import time

def logger(msg):
    def time_master(func):
        def call_func():
            print('开始运行')
            start=time.time()
            func()
            stop=time.time()
            print('运行结束')
            print(f'一共耗费{(stop-start):.2f}秒')
        return call_func
    return time_master


#@logger(msg="A")
def funA():
    time.sleep(1)
    print('正在调用funA')


#@logger(msg="B")
def funB():
    time.sleep(1)
    print('正在调用funB')
#原本的样子
funA=logger(msg='A')(funA)
funB=logger(msg='B')(funB)
funA()
funB()