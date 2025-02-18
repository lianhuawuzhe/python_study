# def myfunc():
#     x=520#仅限于该函数
#     print(x)
# myfunc()

# x=880
# def myfunc():
#     print(x)
# myfunc()


# x=880
# print(id(x))
# def myfunc():
#     x=520#无法在函数中修改全局变量的值
#     print(id(x))
# myfunc()

# x=880
# def myfunc():
#     global x#全局变量声明
#     x=520
#     print(x)
# print(x)
# myfunc()

# def funA():
#     x=520
#     def funB():#无法直接调用funB
#         nonlocal x
#         x=880
#         print('In funB x=',x)
#     funB()
#     print('In funA x=',x)
# funA()
# str='莲华把str给毁了'
# str(520)

