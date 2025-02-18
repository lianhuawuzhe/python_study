import random
anwer=random.randint(1,3)
while 1>0:
    temp=input("""1为剪刀
2为石头
3为布
请打出你要出的手势：""")
    guess=int(temp)
    print("我出的是————")
    if anwer==1:
        print("剪刀")
    if anwer==2:
        print("石头")
    if anwer==3:
        print("布")
              
    if guess==anwer:
        print("平局。")
    if anwer+2>guess>anwer:
        print("你赢了，真厉害！")
    if anwer-2<guess<anwer:
        print("你输了，真可惜。")
    if anwer-2==guess:
        print("你赢了，真厉害！")
    if anwer+2==guess:
        print("你输了，真可惜。")
    print("继续^_^\n")