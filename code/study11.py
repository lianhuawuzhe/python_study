# name=input("你的名字:")
# print("你好，"+name+"!")
# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(sum)
def temp_conversion(c):
    f=c*1.8+32
    return f
c=float(input('请输入摄氏度：'))
f=temp_conversion(c)
print('转化成华氏度是：'+str(f))