def c2f(c):
    f=c*1.8+32
    return f
def f2c(f):
    c=(f-32)/1.8
    return c
print(f'__name_-的值是{__name__}')
if __name__=='__main__':
    print(f'测试，0摄氏度={c2f(0):.2f}华氏度')
    print(f'测试，0华氏度={f2c(0):.2f}摄氏度')
