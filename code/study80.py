# from abc import ABCMeta,abstractmethod
# class fruit(metaclass=ABCMeta):#抽象基类这样写就行了
#     def __init__(self,name):
#         self.name=name
#     @abstractmethod#抽象方法
#     def good(self):
#         pass
# class banana(fruit):
#     def good(self):
#         print('多吃香蕉身体好')
#     pass
# b=banana('香蕉')
# b.good()

from abc import ABCMeta,abstractmethod
class animal(metaclass=ABCMeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def intro(self):
        pass
    @abstractmethod
    def say(self):
        pass

class cat(animal):
    def intro(self):
        print(f'我是一只猫，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('mua')

class dog(animal):
    def intro(self):
        print(f'我是一只狗，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('wow')

class pig(animal):
    def intro(self):
        print(f'我是一只猪，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('en')
c=cat('web',14)
d=dog('lian',12)
c=pig('hua',11)
c.say()