# x='山海自来水来自海上'
# print(x.count('海',0,5))
# print(x.find('海'))
# print(x.rfind('海'))
# print(x.index('龟'))
# code="""
#         print('i love fishc')
#     print('i love my wife')"""
# print(code)
# new_code=code.expandtabs(8)
# print(new_code)
# s = "a\tbcd\tefg\n1\t234\t567"
# print(s.expandtabs())
# print(s.expandtabs(4))
# x='在吗，我在你家楼下，快点下来'
# y=x.replace('在吗','我好想你')
# print(y)
table=str.maketrans('ABCDEFG','1234567')
y='I love FishC'.translate(table)
print(y)
print('I love FishC'.translate(str.maketrans('ABCDEFG','1234567','love')))