{}#dict
{'one'}#set
{'one':1}#dict
{'lianhua','python'}
{s for s in 'lianhua'}
s=set('fishc')
print('c' in s)
for each in s:
    print(each)
set([1,1,2,3,5])
s=[1,1,2,3,5]
len(s)==len(set(s))
s=set('fishc')
s.isdisjoint(set('python'))
s.isdisjoint('java')
s.issubset('fishc.com.cn')
s.issuperset('fish')
#支持多参数
s.union({1,2,3},'python')#并
s.intersection('fish','fi')#交
s.difference('fih','fiv')#差集
#只支持一个参数
s.symmetric_difference('python')#对称差集
#检测
s<=set('fishc')
s<set('fishc.com.cn')#检测真子集
s>set('fishc')#检测真超集
s>=set('fishc')
#求
s|{1,2,3}|set('python')#并
s&set('php')&set('python')#交
s-set('php')-set('python')#差集
s^set('python')#对称差集