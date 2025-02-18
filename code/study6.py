'''用py设计的第一个游戏'''
import random
counts=3
answer=random.randint(1,10)
while counts>0:
    temp=input('猜猜莲华心里想的数字:')
    guess=int(temp)
    if guess==answer:
        print("你是莲华心里的蛔虫")
        break
    else:
        if guess<answer:
            print("猜小了")
        else:
            print("猜大了")
    counts-=1
print("游戏结束")
