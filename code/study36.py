x={'吕布':'口口布','关羽':'关习习'}
b=dict(吕布='口口布',关羽='关习习',刘备='刘baby')
c=dict([('吕布','口口布'),('关羽','关习习'),('刘备','刘baby')])
print(c)
d=dict({'吕布':'口口布','关羽':'关习习'})
e=dict({'吕布':'口口布','关羽':'关习习'},刘备='刘baby')
f=dict(zip(['吕布','关羽','刘备'],['口口布','关习习','刘baby']))
d=dict.fromkeys('fish',250)
d['f']=70
d['c']=67
d.pop('s')
d.pop('g','没有改参数')
d.popitem
del d['i']
del d
d=dict.fromkeys('fishc',250)
d.clear()