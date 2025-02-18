'''用py设计的第一个游戏'''
counts=3
while counts>0:
    temp=input('猜猜莲华心里想的数字:')
    guess=int(temp)
    if guess==8:
        print("你是莲华心里的蛔虫")
        break
    else:
        if guess<8:
            print("猜小了")
        else:
            print("猜大了")
    counts-=1
print("游戏结束")



# counts=3
# while counts>0:
#     print("i love you")
#     counts-=1