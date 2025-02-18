d=dict.fromkeys('fishc')
d['s']=115
d.update({'i':105,'h':104})
d.update(f='70',c='67')

d['c']
d['C']
d.get('C','这里没有C')
d.setdefault('c','code')
keys=d.keys()
values=d.values()
items=d.items()
e=d.copy()
d={'口口布':{'语文':60,'数学':80},'关羽':{'语文':90,'数学':80}}
d['吕布']['数学']
d={'口口布':[60,70,80],'关羽':[80,90,100]}
d['吕布'][1]
d={'F':70,'i':105,'s':115,'h':104,'C':67}
b={v:k for k,v in d.items() if v>100}
d={x:ord(x) for x in "fishc"}
d={x:y for x in [1,3,5] for y in [2,4,6]}
print(d)