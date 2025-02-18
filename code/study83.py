import TC
print(f'32摄氏度={TC.pp.c2f(32):.2f}华氏度')
print(f'99摄氏度={TC.pp.c2f(99):.2f}华氏度')

TC.pp.printx()
print(TC.s)
TC.x=2333
TC.pp.printx()

from TC import *
print(dir())
fc1.sayhi()
fc2.sayhello()