# print(3&4)
# print(bin(2))#获取二进制
# print(3|4)
# print(~3)#补码011 100
# print(3^2)


# #运算对象<<移动位数(不能是负数)
# bin(8)#10000
# 8>>2#10  8//pow(2,2)
# 8>>3#8//pow(2,3)  一定用地板除，因为移位会丢失数据
# 8<<2#100000 8*pow(2,2)


# #math模块
# import math
# print(0.1+0.2==0.3+math.ulp)#3.9版本，打印Ture

# #易错，让对象作为索引值才会触发
# class C:
#     def __index__(self):
#         print('被拦截了')
#         return 3
# c=C()
# s='lianhua'
# # s[c]
# print(s[c])
# bin(c)
# print(bin(c))
