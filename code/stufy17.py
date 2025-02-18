# for each in 'china':
#     print(each)
# i=0
# while i<len('china'):
#     print('china'[i])
#     i+=1
# sum=0
# for i in 10000:
#     sum+=i
# for i in range(11):
#     print(i)
# for i in range(5,10):
#     print(i)
# for i in range(5,10,2):
#     print(i)
# for i in range(10,5,-2):
#     print(i)
# sum=0
# for i in range(1000001):
#     sum+=i
# print(sum)
# import math
# for n in range(2,51):
#     for x in range(2,math.sqrt(n)):
#         if n%x==0:
#             break
#     print(n)

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'=',x,'*',n//x)
            break
    else:
        print(n,'是一个素数')