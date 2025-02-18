# def myfunc(s,vt,o):
#     return ''.join((o,vt,s))
# a=myfunc('我','打了','莲华')
# print(a)
# myfunc(o='我',vt='打了',s='莲华')

# def myfunc(s,vt,o='lianhua'):
#     return ''.join((o,vt,s))
# myfunc('香蕉','吃')
# myfunc('香蕉 ','吃','莲花')#会覆盖


help(sum)
help(abs)#斜杠左侧只能是位置参数，而不是关键词参数，右侧随意
sum([1,2,3],4)
sum([1,2,3],start=4)

def abc(a,/,b,c):
    print(a,b,c)
abc(3,b=2,c=1)

def abc(a,*,b,c):#右侧只能是关键字参数
    print(a,b,c)
