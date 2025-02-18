# print('{:+}{:-}'.format(520,-250))
# print('{:,}'.format(1234))
# print('{:_}'.format(1234))
# print('{:.2f}'.format(3.1415))
# print('{:.2g}'.format(3.1415))
# print('{:.6}'.format('i love you'))
# # print('{:.2}'.format(520))
# print('{:b}'.format(80))
# print('{:c}'.format(80))
# print('{:d}'.format(80))
# print('{:x}'.format(80))
# print('{:o}'.format(80))
# print('{:#b}'.format(80))


# print('{:f}'.format(3.1415))
# print('{:.2%}'.format(0.98))
# print("{:.{prec}f}".format(3.1415,prec=2))
# print('{:{fill}{align}{width}.{prec}{ty}}'.format(3.1415,fill='+',align='^',width=10,prec=3,ty='g'))

year=2021
print('莲华工作室成立于{}年'.format(year))
print(f'莲华工作室成立于{year}年')
print(f'{-520:010}')
fill='+'
align='^'
width=10
prec=3
ty='g'
print(f'{3.1415:{fill}{align}{width}.{prec}{ty}}')