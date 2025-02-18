# class animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def say(self):
#         print(f'我叫{self.name},今年{self.age}岁')

# class Flymixin:
#     def fly(self):
#         print('我还会飞')

# class pig(Flymixin,animal):
#     def special(self):
#         print('我的技能是拱大白菜')

# p=pig('fishc',5)
# p.say()
# p.special()
# p.fly()

class displayer:#第二步
    def display(self,message):
        print(message)

class loggerminxin:
    def log(self,messaage,filename='lodfile.txt'):
        with open(filename,'a') as f:
            f.write(messaage)

    def display(self,message):#第一步
        super().display(message)
        #去父类查找方法，没有，默认object。super依靠，MRO，这里去displayer
        #mysubclass.mro()
        #MRO 的顺序是：mysubclass → loggerminxin → displayer → object。
        self.log(message)#self其实是subclass

class mysubclass(loggerminxin,displayer):#先左后右，第三步
    def log(self,message):
        super().log(message,filename='subclasslog.txt')
        #MRO 的顺序是：mysubclass → loggerminxin → displayer → object。

subclass=mysubclass()#实例化一个个对象
subclass.display('This is a test.')

