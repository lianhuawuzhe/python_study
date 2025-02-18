# if 3<5:
#     print('我在里面')
#     print('我也在里面')
# print('我在外面')
# if 'lianhua'=='小姐姐':
#     print('lianhua是小姐姐')
# else:
#     print('lianhua不是小姐姐')
# score=input('请输入你的分数：')
# score=int(score)
# if 0<=score<60:
#     print('D')
# elif 60<=score<80:
#     print('C')
# elif 80<=score<90:
#     print('B')
# elif 90<=score<100:
#     print('A')
# elif score==100:
#     print('S')
# else:
#     print('请输入0-100间的分数')
# age=16
# if age<18:
#     print('抱歉，未满18岁禁止访问')
# else:
#     print('欢迎您来')
# age=16
# print('抱歉，未满18岁禁止访问') if age<18 else print('欢迎您来')
# a=3
# b=5
# small=a if a<b else b
# print(small)
score=33
level=(
'D'if 0<=score<60 else
'C' if 60<=score<80 else
'B' if 80<=score<90 else
'A' if 90<=score<100 else
'S' if score==100 else
'请输入0-100之间的分值')
print(level)