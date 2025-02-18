# rhyme=(1,2,3,4,5,'上山打老虎')
# print(rhyme)
# # print(rhyme[0])
# # print(rhyme[-1])
# print(rhyme[:])
# print(rhyme[3:])
# print(rhyme[::2])
# print(rhyme[::-1])

# nums=(3,1,9,6,8,3,5,3)
# a=nums.count(3)
# print(a)
# heros='黑寡妇','绿巨人','钢铁侠'
# b=heros.index('绿巨人')
# print(b)
# s=1,2,3
# t=4,5,6
# print(s+t)
# print(s*3)
# w=s,t
# print(w)
# # for each in s:
# #     print(each)
# for x in w:
#     for y in x:
#         print(y)

# s=(1,2,3,4,5)
# p=[each*2 for each in s]
# print(p)
# x=(520)
# print(type(x))
# y=(520,)
# print(type(y))

# t=(123,'china',3.14)
# print(t)
# x,y,z=t
# print(x)
# print(y)
# print(z)
# x,y=10,20
s=[1,2,3]
t=[4,5,6]
w=(s,t)
print(w)
w[0][0]=0
print(w)