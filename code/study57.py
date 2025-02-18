# class Turtle:#用大写字母开头（约定俗成）
#     head=1
#     eyes=2
#     legs=4
#     shell=True

#     def run(self):
#         print('虽然我行动慢，但遇到危险也会狂奔')
#     def crawl(self):
#         print('不积跬步无以至千里')
#     def bite(self):
#         print('我会咬人')
#     def sleep(self):
#         print('ZZZ')
#     def eat(self):
#         print('谁知盘中餐，粒粒皆辛苦')
# t1=Turtle()
# print(t1.head)
# t1.sleep()
# t2=Turtle()
# #修改
# t2.legs=3
# print(t1.legs)
# print(t2.legs)
# #添加属性
# t1.mouth=1
# print(dir(t1))
# print(dir(t2))


# x=520
# type(x)
# y='lianhua'
# type(y)
# class C:
#     def hello():
#         print('hello')
# c=C()
# c.hello()

class C:
    def get_self(self):
        print(self)
c=C()
c.get_self()#打印实例对象本身
