# def funa():
#     x=880
#     def funb():
#         print(x)
#     return funb#函数只有定义和调用用括号
# funa()()#相当于调用了funb
# #funa（）得到funb的一个引用
# funny=funa()
# funny()
# #对于嵌套函数，外层作用域的变量以某种方式保存，不像局部作用域直接消失

# def power(exp):
#     def exp_of(base):
#         return base**exp
#     return exp_of
# square=power(2)#记住了exp=2
# cube=power(3)#记住了exp=3
# print(square(2))
# print(cube(5))

# def outer():
#     x=0
#     y=0
#     def inner(x1,y1):
#         nonlocal x,y 
#         x+=x1
#         y+=y1
#         print(f'现在，x={x},y={y}')
#     return inner
# move=outer()
# print(move(1,2))
# print(move(-2,2))

