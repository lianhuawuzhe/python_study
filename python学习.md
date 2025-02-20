[TOC]

# python学习

## 1.用python设计第一个游戏

### 1.==常见错误==

1.标点需要全为英文

2.缩进不正确

3.函数编写是否正确

### 2.查看内置函数

`dir(_builtins_)`

## 2.变量和字符串（上)

### 1.变量名

字母，数字，下划线，不以数字开头，python3支持中文

## 2.交换变量值

```
x=3

y=5

x,y=y,x

print(x,y)
```



### 3.字符串

用引号区别于变量名

单引号

双引号

三引号

要成双成对

==转义字符（反斜杠）==

`print('\"Life is short,let\'s learn python.\"')`

\n换行

## 2.变量和字符串（下）

### 1.原始字符串r

```
print("D:\three\two\one\now")

print("D:\\three\\two\\one\\now")

print(==r=="D:\three\two\one\now")
```



### 2.反斜杠

反斜杠放在字符串末尾表明字符串还没完如果没有反斜杠直接enter会报错

```
print("i love china\n\
	and you")

print("i love china\n
	and you")
```



### 3.长字符串

用三引号(前后呼应，成双成对)

用它就不用反斜杠了

### 4.字符串的加法和乘法

#### 1.加法

字符串是拼接

#### 2.乘法

字符串是复制

## 4.是时候讲代码了

### 1.说明文档

开头三引号

### 2.int()不能将中文转化成数字

### 3.比较运算符

if guess==8:

else:

< >= != 

is(判断两个对象的id是否相等)

is not(判断两个对象是否不等)

## 5.改进小游戏（上）

### 1.分支结构

if else

### 2.循环结构

while 条件：

break用于跳出一层循环体

## 6.改进小游戏（下）

### 1.引用模块

import 模块名

random生成伪随机数

因为其随机数可以重现，对伪随机数数攻击需要要拿到种子，默认是系统时间

用cmd

>>> import random

>>> x=random.getstate()
>>> print(x)
>>>
>>> random.randint(1,10)
>>> 7
>>> random.randint(1,10)
>>> 3
>>> random.randint(1,10)
>>> 7
>>> random.randint(1,10)
>>> 5
>>> random.randint(1,10)
>>> 1
>>> random.randint(1,10)
>>> 7
>>> random.setstate(x)
>>> random.randint(1,10)
>>> 7
>>> random.randint(1,10)
>>> 3
>>> random.randint(1,10)
>>> 7
>>> random.randint(1,10)
>>> 5
>>> random.randint(1,10)
>>> 1

## 7.数字类型（上）

### 1.整数

长度不受限制（相除得到小数）

### 2.浮点数

不是精确的，比较的时候要注意

0.3<0.1+0.2

#### 1.如何精确计算浮点数？

```
import decimal
a=decimal.Decimal('0.1')
==b=decimal.Decimal('0.2')
print(a+b)
c=decimal.Decimal('0.3')
if a+b=c:
  print('true')
```



#### 2.E记法

0.00005

5e-05

### 3.复数

实部虚部(注意：实部虚部都是浮点数)

1+2j

x=1+2j

print(x.real)

print(x.imag)

## 8.数字类型（下）

### 1.加减乘除

+-*/都是正常的

### 2.//  % divmod(x,y)

// 地板除，区别于C语言中的除（直接去掉小数部分），向下取整，

-3//2得到-2

% 两数相除的余数

divmod(x,y) X==(x//y)*y+(x%y)

返回（x//y,x%y）

### 3.-x +x

### 4.abs(x)

返回绝对值

==传入复数，返回复数的模==

### 5.int(x)  float(x) complex(x)

#### 1.int(x)

 将指定的数转换为整数

浮点数直接去掉小数部分（不是四舍五入）

#### 2.float(x)

 转化为浮点数

print(float(520))

print(float('14'))

print(float('+1E6'))

print(float('-1E06'))

#### 3.complex(x)

转化为复数

print('1+2j')注意复数内部不要有空格

### 6.pow(x,y) x**y

计算x的y次方

pow(x,y,z)即x**y%z

## 9.布尔类型（其实是特殊的整数类型）

bool(False)为false

bool("字符串")只有为空字符串才是false

bool(0) bool(0.0) bool(0j)为false

#### ==1.为false的情况==

1.定义为false的对象：None和False

2.值为0的数字类型：0，0.0，0j,Decimal(0),Fraction(0,1)(分子为0，分母为1的有理数)

3.空的序列和集合：'',(),{},[],set(),range(0)

#### 2.逻辑运算符(布尔运算)

运算对象是布尔类型的对象

and print(3<4 and 4<5)

or

not，得到和操作数相反的布尔类型

print(not True)

print(not 520)

print(not 0)

python中任何对象都能直接进行真值测试

## 10.短路逻辑和运算符优先级

### 1.短路逻辑

直接把影响结果的操作数扔出来

4 or 5直接得到5

### 2.运算符优先级

1+2>3-4得到true

==lambda==

==if else==

==or==

==and== 

==not==

==比较运算符（is，not,is not,>=,==,!=）==

==|==

==^==

==&==

==<<,>>==

==+,-==

## 11.谋定而后得，知止而有得（上）

### 流程图（至上而下）

没有严格的语法要求

摄氏度转华氏度

## 12.谋定而后得，知止而有得（下）

### 思维导图（心智图，发散思维）

用mindmanager

## 13.了不起的循环和分支（1）

### 1.分支语句

#### 1.

if condition:

​    statement(s)

==缩进决定了从属关系==

==同一个代码块每一个语句缩进量都是相同的==

#### 2.

if condition:

​    statement(s)

else:

   statement(s)

#### 3.可增加效率

if condition1:

   statement(s)

elif condition2:

   statement(s)

elif condition3:

   statement(s)

前面不成立才判断后面

#### 4.

if condition1:

   statement(s)

elif condition2:

   statement(s)

elif condition3:

   statement(s)

else:

   statement(s)

#### 5.容易将语句打入内部

条件成立时执行的语句if condition else 条件不成立时执行的语句

a=3

b=5

small=a if a<b else b

print(small)

==用什么形式取决于项目的复杂度==

score=33

level=(

'D'if 0<=score<60 else

'C' if 60<=score<80 else

'B' if 80<=score<90 else

'A' if 90<=score<100 else

'S' if score==100 else

'请输入0-100之间的分值')

print(level)

==多行表示除了反斜杠也可以用括号括起来==

## 14.了不起的循环和分支（2）

分支结构的嵌套

可以嵌套无数多次

## 15.了不起的循环和分支（3）

### 循环结构

#### while

while condition:

   statement(s)

小心死循环

#### break

执行之后不管后面的语句

## 16.了不起的循环和分支（4）

### 1.循环结构

#### continue

只会跳出本次循环

#### else

==当循环条件不为真时，else才被执行==

i=1

while i<5:

  print('循环内，i的值是',i)

  if i==2:

​    break

  i+=1

else:

  print('循环外，i的值是',i)

else不会被执行

可以用于检测循环退出的情况

### 2.循环结构的嵌套

==break和continue都只能作用于一层循环==

![QQ_1739128120935](pytohn学习.assets/QQ_1739128120935.png)

## 17.了不起的循环和分支（5）

for 变量 in 可迭代对象(元素能够单独被提取出来的对象，字符串)：

   statement(s)

==len()用于获取一个对象的长度==

==range()帮你生成一个数字序列,参数只能是整形==

==range(stop)==

==range(start,stop)==

==range(start,stop,step)==

==这里的stop不会被打出来，而start会==

for i in range(10,5,-2):

  print(i)

## 18.列表（1）

### 1.创建列表

### 2.下标访问元素

print(rhyme[-1])

==可以用-1访问最后一个元素，依此类推==

### 3.列表切片

## 19.列表（2）

### 1.增

heros=['钢铁侠','绿巨人']

#### 1.

==heros.append==('黑寡妇')

print(heros)

#### 2.

==heros.extend==(['灭霸','鹰眼','雷神'])

==extend()的方法必须是一个可迭代对象==

print(heros)

#### 3.切片

s=[1,2,3,4,5]

s[len(s):]=[6]

print(s)

==s[len(s):]=[7,8,9]==相当于s.extend([7,8,9])

print(s)

#### 4.

insert(位置，元素)

### 2.删

#### 1.

==s.remove（）==

注意：1.如果有多个匹配的元素，删除下标最小的

2.若没有元素，则报错

#### 2.

==pop(下标)删除指定元素==

#### 3.

==s.clear()清空列表元素==

## 20.列表（3）

### 3.改

列表是可变的，而字符串是不可变的

#### 1.下标索引直接改

#### 2.切片

![QQ_1739168510597](pytohn学习.assets/QQ_1739168510597.png)

heros=['灭霸','钢铁侠','雷神','钢铁侠','绿巨人']

heros[1]='黑寡妇'

print(heros)

heros[1:3]=['武松','林冲']

print(heros)



#### 3.排序

nums=[3,1,6,7,8,8,3,4,5]

==nums.sort()==排序

==nums.reverse()==倒转顺序

==nums.sort(reverse=True)==效果和上面两个一起用一样

### 4.查

查找多少个==.count==

查找下标==heros.index('绿巨人')==，若有多个元素，返回第一个下标索引

index(x,start,end)

![QQ_1739169525322](pytohn学习.assets/QQ_1739169525322.png)

==copy()用于拷贝列表====，也可用切片==

nums_copy1=nums.copy()

nums_copy2=nums[1:4]

print(nums_copy1)

print(nums_copy2)

## 21.列表（4）



### 1.加法和乘法

加法：拼接

乘法：复制

### 2.嵌套列表

matrix(矩阵)

#### 1.访问嵌套列表

嵌套循环

matrix=[[1,2,3],

[4,5,6],

[7,8,9]]

print(matrix)

for i in matrix:

  for each in i:

​    print(each,end='')

  print()

#### ==2.用循环语句创建并初始化二维列表==

容易出高级bug

引入is(两个变量是否指向同一对象)

字符串不可变（开辟一个位置），列表可变（开辟两个位置）

A=[0]*3

for i in range(3):

  A[i]=[0]*3

print(A)

C=[[0]*3]*3

A[1][1]=1

C[1][1]=1

去看源代码

==C试图对一个嵌套列表进行拷贝，但是并不是拷贝，只是对同一个列表的引用==

## 22.列表（5）

变量不是盒子

复制只是引用

要得到独立的列表还是要拷贝

### 1.浅拷贝

copy,切片，==无法处理嵌套列表，浅拷贝只是拷贝了外层对象==

==如果包含嵌套对象只是拷贝其引用==

### 2.深拷贝

用模块

import copy

==浅拷贝y=copy,copy(x)==

==深拷贝y=copy.deepcopy(x)==效率较低

## 23.列表（6）

### 1.列表推导式

效率高出一倍,结果是一个列表,也可以用于处理字符串

==[expression for target in iterable]==

x=[i+1 for i in range(10)]

print(x)

x=[]

for i in range(10):

  x.append(i+1)

print(x)

y=[c*2 for c in 'china']

print(y)

code=[ord(c) for c in "china"]==ord()将单个字符转化为对应编码==

print(code)



下面是对二维列表的各种提取

matrix=[[1,2,3]

,[4,5,6]

,[7,8,9]]

col2=[row[1] for row in matrix]

print(col2)

diag=[matrix[i][i] for i in range(len(matrix))]

print(len(matrix))

p=[matrix[i][2-i] for i in range(len(matrix))]

print(p)

### 2.列表推导式和循环的区别

列表推导式直接创建一个新的列表

循环是遍历修改元素

## 24.列表（7）

### 1.创建二维列表

1.循环

2.列表推导式

S=[[0]*3 for i in range(3)]

print(S)

### 2.高阶知识

==[expression for target in iterable if condition]==

==注：先执行for,再执行if，最后执行左侧表达式==

#### 1.列表推导式的嵌套

==[expression for target1 in iterable1==

==for target2 in iterable2==

==…==

==]==

matrix=[[1,2,3],[4,5,6],[7,8,9]]

flatten=[col for row in matrix for col in row]

print(flatten)

flatten=[]

for row in matrix:

  for col in row:

​    flatten.append(col)

print(flatten)

##### 笛卡尔乘积

某个变量是临时的或无关紧要的，用下划线充当变量名

p=[x+y for x in 'fishc' for y in 'FISHC']

print(p)

_=[]

for x in 'fishc':

  for y in 'FISHC':

​    _.append(x+y)

print(_)

#### 2.列表推导终极语法

==[expression for target1 in iterable if condition1==

==for target2 in iterable2 if condition2==

==…]==

p=[[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0]

print(p)

_=[]

for x in range(10):

  if x%2==0:

​    for y in range(10):

​      if y%3==0:

​        _.append([x,y])

print(_)

#### 3.kiss原则

简洁胜于复杂，列表推导维护和阅读代码的成本太高

## 25.元组

有关序列，目前，列表，字符串，元组

列表[factor1,factor2,factor3]

### 1.元组可进行的操作

==元组（factor1,factor2,factor3）====,也可以去掉括号，可以通过下标获取元素==

==元组内容不可改变，不可修改==

rhyme=(1,2,3,4,5,'上山打老虎')

print(rhyme)

print(rhyme[0])

print(rhyme[-1])

==可进行切片操作==（将目标对象的元素以一种特定方式导出，而不是修改）

### 2.查

#### 1.count

#### 2.index

### 3.拼接和重复

+和*

### 4.元组的嵌套

s=1,2,3

t=4,5,6

print(s+t)

print(s*3)

w=s,t

### 5.元组的迭代

for x in w:

  for y in x:

​    print(y)

### 6.列表推导式对元组进行转换

不存在元组推导式

s=(1,2,3,4,5)，==改为圆括号是生成器==

p=[each*2 for each in s]

print(p)

### 7.如何生成只有一个元素的元组

x=(520)

print(==type(x)==)

int类型

x=(520,)才对

### 8.打包和解包

t=(123,'china',3.14)

print(t)

x,y,z=t

print(x)

print(y)

print(z)

==该行为适合于任何序列类型==

t=[123,'china',3.14]

x,y,z=t

print(x)

print(y)

print(z)

a,b,c,d,e='china'

print(a)

print(b)

print(c)

print(d)

print(e)

==注意解包左右元素个数一致==

炫技：

a,b,==*c==='fishc'

print(a)

print(b)

print(c)

### 9.多重赋值

x,y=10,20

背后逻辑

_=(10,20)

x,y=_

_表示匿名变量

### 10.修改元组

s=[1,2,3]

t=[4,5,6]

w=(s,t)

print(w)

w[0][0]=0

print(w)

==元组固然不可修改，但是其元素为可变列表就可以修改==

## 26.字符串（1）

判断回文数

x='12321'

print('是回文数') if x==x[::-1] else print('不是回文数')

字符串的各种方法更快更安全

### 1.大小写字母换来换去

capitalize()返回字符串将首字母变成大写，其余变为小写

casefold()返回字符串全变为小写，可处理其他语言

titile()每个单词首字母变成大写，其余小写

swapcase()大小写翻转

upper()全变为大写

lower()全变为小写，只处理英语

### 2.左中右对齐

center(width,fillchar='')放中间

ljust(width,fillchar='')左对齐

rjust(width,fillchar='')右对齐

zfill(width)左边全加上0，负号移到最左边

width指定宽度，若小于等于原字符串，直接输出

fillchar指定符号，默认空格

## 27.字符串（2）

### 3.查找

==count（sub[,start[,end]]）==

x='山海自来水来自海上'

print(x.count('海',0,5))

==找不到返回-1==

==find(sub[,start[,end]])从左往右找==

==rfind(sub[,start[,end]])从右往左找==



==找不到异常==

==index(sub[,start[,end]])==

==rindex(sub[,start[,end]])==

### 4.替换

==expandtabs([tabsize=8])用空格代替制表符，返回新的字符串==

![QQ_1739202921681](pytohn学习.assets/QQ_1739202921681.png)

==replace(old,new,count=-1)==

不设置count的参数的话，默认替换全部

==translate(table)==table为转换规则的表格

table===str.maketrans==('ABCDEFG','1234567')

y='I love FishC'.translate(table)

print(y)

也可以直接

print('I love FishC'.translate(str.maketrans('ABCDEFG','1234567'，==’love'==)))

第三个参数为将指定参数忽略

### 28.字符串（3）判断，返回布尔类型

懒得记了，去查用法

1.startswith(prefix[,start[,end]])

2.endswith(suffix[,start[,end]])

方括号为可选参数

参数支持元组

3.istitle()

判断字符串中单词都以大写字母开头，其余都为小写

4.isupper（）判断全为大写

print('I love Python'.upper().isupper())

连续调用多个方法，从左往右依次调用

5.islower（）判断全为小写

6.isalpha()判断是否全为字母

7.isspace()检测空白字符串

\t,空格，\n

8.isprintable()判断是否都可以打印

==转义字符\n不能被打印==

下面三个都是判断是否为数字

==9.isdecimal()，一个数的平方是false,罗马数字false,中文alse,繁体false==

==10.isdigital()罗马数字false,中文false,繁体false==

==11.isnumeric()==

12.isalnum()

集大成者，isalpha,isdecimal,isdigit,isnumeric有一个为true即为true

13.isidentifier()判断字符串是否是合法的python标识符

下划线，数字，字母，数字不放开头

14.import keyword

keyword.iskeyword('if')

## 29.字符串（3）截取

### 1.方法

1.lsrtip(chars=None)去除左侧空白,可修改None

2.rstrip()去除右侧空白

3.strip()左右不要留白

print('www.ilovefishc.com'.lstrip('wcom.'))

print('www.ilovefishc.com'.rstrip('wcom.'))

print('www.ilove fishc.com'.strip('wcom.'))

按照单个字符为单位进行匹配去剔除，依次寻找

4.removeprefix(prefix)（3.8以及以下版本不行）

remivesuffix(suffix)

允许指定将要删除的前缀和后缀，匹配参数指定的整个字符串

==3.4.易混淆==

### ==2.拆分和拼接==

### 1.拆分

1.partition(sep)(找分割符，返回三元组)

2.rpartition(step)

3.split(step=None,maxsplit=-1)

rsplit(s,c)

返回列表，第一个参数指定分割符，后一个参数为切割次数，-1为找到就切

4.splilines(keepends=False)

返回结果，False不包含换行符，改为True包含

列表换回，按行分割

print('苟日新\r又日新\n\r日日新'.splitlines())

### 2.拼接

==5.join(iterable)==

print('.'.join(['www','ilovefishc','com']))

用列表或者元组包裹参都可以

print(''.join('fishc','fishc))

join效率更高（大数据）

## 30.字符串（5）字符串格式化的方法

### 1.format

print('1+2={}，2的平方是{}，3的立方是{}'.format(1+2,2*2,3*3*3))

花括号是用来占位的

#### 1.参数

print('{==1==}看到{==0==}就很激动！'.format('莲华','漂亮的小姐姐'))

==参数中的字符串会被当成元组中的元素对待==

#### 2.多次引用：

print('{0}{0}{1}{1}'.format('是','非'))

#### 3.关键字索引

print('我叫{name}，我爱{fav}'.format(fav='python',name='lianhua'))

#### 4.位置和关键词索引可以混用

#### 5.输出花括号

print('{},{},{}'.format(1,{},2))参数花括号

print('{},{{}},{}'.format (1,2))花括号注释花括号

### 2.align(对齐的方式)

<,>,=（强制将填充放置在符号（如果有）之后数字之前的位置),^(强制居中)

width指定宽度

print('{1:>10}{0:<10}'.format(520,250))

位置索引，对齐方向，显示宽度

[[fill]]align][sign][#][0][width][grouping_option][.precision][type]

查看源代码

print('{:==0==10}'.format(-520))填充0，感知正负号

print('{:010}'.format('lianhua'))报错，只对数字有用

print('{1:%>10}{0:%<10}'.format(520,250))

print('{:0=10}'.format(-520))

## 31.字符串（6）继续格式化

### 1.符号选项

+

-（加不加都可以）

空格（正数空格，负数负号）

### 2.千分符

，(千分符)

下横线（千分符)

位数不足，不显示千分符

### 3.精度

[type]设置为f或F时，是显示小数点后多少位

gG小数点前后一共

非数字限定最大字段的大小

整数不允许用[.precision]

### 4.type（整数）

b二进制

c Unicode

d十进制

o八进制

xX十六进制

n和d类似，会使用当前语言环境设置的分隔符插入到恰当位置

None和d一样

print('{:==#==b}'.format(80))加上#会显示格式

### 5.type(浮点数和复数)

传入整数会转化成等值浮点数

e科学计数法

E

f默认六个小数位,不是数nan，无穷inf

F NAN INF

g(小数f,大数e)

G(小数F，大数E)

%(百分形式输出，六个小数位)

print('{:.2%}'.format(0.98))

None类似于g(区别自己查)

==关键字参数==

print("{:.{prec}f}".format(3.1415,prec=2))

==print('{:{fill}{align}{width}.{prec}{ty}}'.format(3.1415,fill='+',align='^',width=10,prec=3,ty='g'))==

### 6.f-字符串（3.6以上版本）

语法糖

前缀f F

print(f'莲华工作室成立于{year}年')

print(f'{-520:010}')

fill='+'

align='^'

width=10

prec=3

ty='g'

print(f'{3.1415:{fill}{align}{width}.{prec}{ty}}')

## 32.序列（上）

1.都可以索引，第一个为0

2.都可以切片

3.很多共同的运算符

可变序列

不可变序列

### 1.+ *

对象的身份证id（），==唯一标识==，不可修改，不会有重复的值

增量赋值改变不可变序列的id，不改变可改变序列的id

### 2.is is not

同一性运算符，判断是否为同一对象

### 3.in not in

判断包含问题

print('lian' in 'lianhua')

### 4.del

删除一个或多个指定对象

x='fishc'

y=[1,2]

del x,y

print(x)

print(y)

报错

==删除可变序列中指定元素，切片也可以==

del

x=[1,2,3,4,5]

del x[1:4]

print(x)

切片

y=[1,2,3,4,5]

y[1:4]=[]

print(y)

切片解决不了

x=[1,2,3,4,5]

del x[::2]

print(x)

clear（）的实现

```python
x=[1,2,3,4,5]
x.clear()
print(x)
y=[1,2,3,4,5]
del y[:]
print(y)
```



## 33.序列（中）函数

### 1.转换

list()转化成列表

tuple()

str()只是在外围加引号

### 2.

max()

min()

![QQ_1739262649156](pytohn学习.assets/QQ_1739262649156.png)

直接传参

print(max(1,2,3,8,0))

### 3.

len()有范围

b=len(range(2**100))报错，2^31-1

sum(可迭代对象，start=x)从x开始加

print(sum(s,start=100))

### 4.

方法只适用于列表，函数用于可迭代对象

sorted(可迭代对象 ，key,reverse=False)(默认)返回列表

s=[1,2,3,0,6]

print(sorted(s))

print(s)全新列表，不改变s

![QQ_1739267058230](pytohn学习.assets/QQ_1739267058230.png)

![QQ_1739267223351](pytohn学习.assets/QQ_1739267223351.png)



reversed(可迭代对象)返回迭代器，暂时理解为可迭代对象

![QQ_1739276842689](pytohn学习.assets/QQ_1739276842689.png)

print(list(reversed('lianhua')))

## 34.序列（下）

### 1.all any

all()判断是否所有元素都为真

any()判断有一个为真

### 2.enumerate()

enumerate()返回一个枚举对象

![QQ_1739277352760](pytohn学习.assets/QQ_1739277352760.png)

![QQ_1739277362594](pytohn学习.assets/QQ_1739277362594.png)



### 3.zip常用1

zip()

![QQ_1739277587459](pytohn学习.assets/QQ_1739277587459.png)

==长度不一样以短的为准==，丢弃后面的

plus版本

![QQ_1739277801201](pytohn学习.assets/QQ_1739277801201.png)

### 4.map常用2

map(函数，参数)返回包含计算结果的迭代器

ord获取编码

```python
mapped=map(ord,'Fishc')
c=list(mapped)
print(c)

mapped=map(pow,[2,3,10],[5,2,3])
print(list(mapped))
```

==长度不一样以短的为准==，丢弃后面的

```
print(list(map(max,[1,3,5],[2,2,2],[0,3,9,8])))
```

### 5.filter()常用3

fillter()返回结果为真的元素构成的迭代器

print(list(filter(str.islower,'FishC')))

### 6.迭代器VS可迭代对象

迭代器一定是可迭代对象

迭代器一次性，可迭代对象可重复使用

```python
mapped=map(ord,'FishC')
for each in mapped:
    print(each)
print(list(mapped))
```

#### 1.iter()

把可迭代对象转换成迭代器

```python
x=[1,2,3,4,5]
y=iter(x)
print(type(x))
print(type(y))
```

#### 2.next()

将迭代器中元素提取出来

异常（故意留下）是可控的，错误是不可控的

下面发生异常

![QQ_1739281170862](pytohn学习.assets/QQ_1739281170862.png)

改进：

```python
x=[1,2,3,4,5]
y=iter(x)
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
print(next(y,'没啦，被你掏空了'))
```

## 35.字典（上)

### 1.首先用列表模拟映射关系

 破译摩斯密码

#密文列表

#明文列表

方法一：

```python
c_table=[]
d_table=[]
code=input('请输入摩斯密码：')
split_code=code.split(' ')#用于将字符串按照空格字符拆分成多个子字符串，并返回一个包含这些子字符串的列表。
result=[d_table[c_table.index(each)] for each in split_code]
print(result)
# for each in split_code:
#     _=c_table.index(each)
#     result.append(d_table[_])

```

方法二：

放到一个列表，+1

### 2.字典

效率：字典<2个列表<1个列表

## 36.字典（中）

x={'键':'值','关羽':'关习习'}

### 1.字典的创建

#### 1.

```
x={'吕布':'口口布','关羽':'关习习'}
```

#### 2.

```
b=dict(吕布='口口布',关羽='关习习',刘备='刘baby')
```

注意：键上不要加引号

#### 3.用列表

```python
c=dict([('吕布','口口布'),('关羽','关习习'),('刘备','刘baby')])
```

#### 4.

```
d=dict({'吕布':'口口布','关羽':'关习习'})

```

#### 5.

```
e=dict({'吕布':'口口布','关羽':'关习习'},刘备='刘baby')

```

不要引号

### 6.

```
f=dict(zip(['吕布','关羽','刘备'],['口口布','关习习','刘baby']))

```

六种方法等价

### 2.方法(3.7之后字典有顺序)

#### 1.增

fromkeys(iterable[,values])

初始化，修改

```python
d=dict.fromkeys('fish',250)
d['f']=70
d['c']=67#增加
```

序列中元素可以重复

键不可以重复

#### 2.删

pop(key[,default])

```
d.pop('s')
d.pop('g','没有改参数')
```

popitem()3.7之后删除最后一个键值对

```
d.popitem
```

del关键字

```
del d['i']
del d#删除字典
```

clear()清空

```
d=dict.fromkeys('fishc',250)
d.clear()
```

## 37.字典（下）

### 3.改

update([other])

```
d.update({'i':105,'h':104})

d.update(f='70',c='67')
```

### 4.查

```
d['c']
d['C']
```

get(key[,default])

```
d.get('C','这里没有C')
```

setdefault(key[,default])返回值，若没有，新加入字典

```
d.setdefault('c','code')
d.setdefault('C','code')
```

### 5.获取视图对象

items（）键值对

keys()键

values()值

```
keys=d.keys()
values=d.values()
items=d.items()
```

### 6.拷贝

浅拷贝

```
e=d.copy()
```

### 7.函数

len(d)获取键值对数量

"c" in d

"C" not in d

list(d)得到键

list(d.values())

iter(d)获取迭代器

3.8版本可用

list(reversed(d.values))逆向排序

### 8.嵌套

```
d={'口口布':{'语文':60,'数学':80},'关羽':{'语文':90,'数学':80}}
d['吕布']['数学']
d={'口口布':[60,70,80],'关羽':[80,90,100]}
d['吕布'][1]
```

### 9.字典推导式

```
d={'F':70,'i':105,'s':115,'h':104,'C':67}
b={v:k for k,v in d.items() if v>100}
d={x:ord(x) for x in "fishc"}

```

```
d={x:y for x in [1,3,5] for y in [2,4,6]}
print(d)
```

## 38.集合

唯一

无序（不用下标）

```
{}#dict
{'one'}#set
{'one':1}#dict
```

### 1.创建集合

1.直接

2.集合推导式

{s for s in 'lianhua'}

3.类型构造器

set('fishc')

```
print('c' in s)

```



### 2.访问集合元素

迭代

```
for each in s:
    print(each)
```

### 3.去重（唯一性）

```
set([1,1,2,3,5])
```

判断是否有重

```
len(s)==len(set(s))
```

### 4.浅拷贝

1.检测两个集合是否相关

```
s=set('fishc')
s.isdisjoint(set('python'))
s.isdisjoint('java')
```

2.检测子集

```
s.issubset('fishc.com.cn')

```

3.检测超集

```
s.issuperset('fish')

```

4.生成新集合（方法，可使用任何可迭代的对象）

```
#支持多参数
s.union({1,2,3},'python')#并
s.intersection('fish','fi')#交
s.difference('fih','fiv')#差集
#只支持一个参数
s.symmetric_difference('python')#对称差集
```

5.运算（只使用集合）

```python
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
```

## 39.集合（下）

可变set

不可变frozenset

上节课的方法以上都适用

以下方法只适用于set

### 1.update(*others)

others多个参数，other一个

intersection_update(*others)

difference_update(*others)

symmetric_difference_update(*others)

```python
s=set('fishc')
s.update([1,1],'23')#f,i,s,h,c,1,2,3，迭代
s.intersection_update('fishc')#交
s.difference_update('php','python')#差集
s.symmetric_difference_update('python')#对称差集
```



### 2.

```python
#增加
s.add('45')
#删
s.remove('服了')#不存在会报错
s.discard('服了')#不存在会静默处理
s.pop()#随机弹出一个元素
s.clear()#清空
```



### 3.可哈希

```
#整数哈希值等于自身
hash(1.0)
#值相等哈希值相等
hash(1)
hash(1.001)
```

python的可变大多不可哈希

不可变可哈希

可哈希对象才能作为字典的键和集合的元素

#### 实现集合嵌套

错误：集合是可变容器

```
x={1,2,3}
y={x,3,4}
```

正确

```
x=frozenset(x)
y={x,3,4}
```

列表（遍历)变成集合（索引）后效率很高，空间换时间

## 40.函数（1）

打包代码

### 1.创建和调用函数

形式参数，实际参数

```
def myfunc():
    pass#空语句，占位符
myfunc()
def myfunc():
    for i in range(3):
        print('I love lianhua')
myfunc()
def myfunc(name,times):#形参
    for i in range(times):
        print(f'I love {name}.')
myfunc('python',5)#实参
```

### 2.函数返回值

```
def div(x,y):
    if y==0:
        return '除数不能为0'
    else:
        return x/y#执行return后马上退出
div(4,2)
```

```
def myfunc():
    pass
print(myfunc())
```

没有return返回None

## 41.函数（2）

### 1.位置参数

```
def myfunc(s,vt,o):
    return ''.join((o,vt,s))
a=myfunc('我','打了','莲华')
print(a)
```

### 2.关键字参数

```
myfunc(o='我',vt='打了',s='莲华')

```

混合使用：位置参数必须在关键字参数之前

### 3.默认参数

默认参数应该放在最后

```
def myfunc(s,vt,o='lianhua'):
    return ''.join((o,vt,s))
myfunc('香蕉','吃')
myfunc('香蕉 ','吃','莲花')#会覆盖
```

### 4.冷门知识点

指定位置参数

```
help(sum)
help(abs)#斜杠左侧只能是位置参数，而不是关键词参数，右侧随意
sum([1,2,3],4)
sum([1,2,3],start=4)

def abc(a,/,b,c):
    print(a,b,c)
abc(3,b=2,c=1)
```

指定关键字参数

```
def abc(a,*,b,c):#右侧只能是关键字参数
    print(a,b,c)
```

## 42.函数（3）

参数个数不限制

### 1.收集参数

定义：

```python
print('lianhua')
print('lianhua','爱','python')
def myfunc(*args):
    print('有{}个参数'.format(len(args)))
    print('第二个参数是：{}'.format(args[1]))
    print(args)#元组有打包和解包的能力
myfunc('lianhua','python',1,2,3)
def myfunc():
    return 1,2,3
print(myfunc())
x,y,z=myfunc()
print(x)
print(y)
print(z)
#函数参数通过星号实现打包操作，实际是元组
```

```
def myfunc(*args,a,b):#收集参数后面必须使用关键字参数
    print(args,a,b)
myfunc(1,2,3,a=4,b=5)
```

回顾：

```
def abc(a,*,b,c):#*为匿名的收集参数
    print(a,b,c)
abc(1,b=2,c=3)

```

```
def myfunc(**kwargs):#把参数打包成字典
    print(kwargs)
myfunc(a=1,b=2,c=3)
```

```
#混合使用
def myfunc(a,*b,**c):
    print(a,b,c)
myfunc(1,2,3,4,x=5,y=6)
```

回顾：

![QQ_1739332799922](pytohn学习.assets/QQ_1739332799922.png)

![QQ_1739332810226](pytohn学习.assets/QQ_1739332810226.png)

### 2.解包参数

形参：参数的打包

实参：解包

```
args=(1,2,3,4)
def myfunc(a,b,c,d):
    print(a,b,c,d)
print(myfunc(*args))#解包

kwargs={'a':1,'b':2,'c':3,'d':4}
print(myfunc(**kwargs))#关键字参数
```

## 43.函数（4）

作用域

### 1.局部作用域

```
def myfunc():
    x=520#仅限于该函数
    print(x)
myfunc()
```



### 2.全局作用域

全局变量，在任何函数外，在函数中，局部优先，同名不同样

```
x=880
def myfunc():
    print(x)
myfunc()
```

```
x=880
print(id(x))
def myfunc():
    x=520#无法在函数中修改全局变量的值,局部变量覆盖
    print(id(x))
```

![QQ_1739334085335](pytohn学习.assets/QQ_1739334085335.png)

### 3.修改全局变量

global

```
x=880
def myfunc():
    global x#全局变量声明
    x=520
    print(x)
print(x)
myfunc()
```

### 4.嵌套函数

作用域和上面类似

```
def funA():
    x=520
    def funB():#无法直接调用funB
        x=880
        print('In funB x=',x)
    funB()
    print('In funA x=',x)
funA()
```

![QQ_1739334944650](pytohn学习.assets/QQ_1739334944650.png)

在内部函数修改外部函数的变量

nonlocal

```
def funA():
    x=520
    def funB():#无法直接调用funB
        nonlocal x
        x=880
        print('In funB x=',x)
    funB()
    print('In funA x=',x)
funA()
```

![QQ_1739335046805](pytohn学习.assets/QQ_1739335046805.png)

### 5.LEGB原则

L：局部作用域

E:外层函数作用域

G:全局作用域

B:![QQ_1739335407870](pytohn学习.assets/QQ_1739335407870.png)

易错

## 44.函数（5）

闭包

引入

```
def funa():
    x=880
    def funb():
        print(x)
    return funb#函数只有定义和调用用括号
funa()()#相当于调用了funb
#funa（）得到funb的一个引用
funny=funa()
funny()
#对于嵌套函数，外层作用域的变量以某种方式保存，不像局部作用域直接消失
```

实现

```python
def power(exp):
    def exp_of(base):
        return base**exp
    return exp_of
square=power(2)#记住了exp=2
cube=power(3)#记住了exp=3
print(square(2))
print(cube(5))

def outer():
    x=0
    y=0
    def inner(x1,y1):
        nonlocal x,y 
        x+=x1
        y+=y1
        print(f'现在，x={x},y={y}')
    return inner
move=outer()
print(move(1,2))
print(move(-2,2))
```

实例：保护游戏角色移动位置，不能被其他函数修改

==1.利用嵌套函数的外层作用域有记忆功能，让数据保存至外层函数的参数或变量中==

==2.将内层函数作为返回值给返回，就可以从外部直接调用到内层函数==

## 45.函数（6）

### 1.将函数作为函数参数

```python
def myfunc():
    print('正在调用myfunc')
def report(func):
    print('主人，我要开始调用函数了')
    func()
    print("主人，我调用完函数了")
report(myfunc)
```

时间管理大师函数

```python
###时间管理大师函数
import time
def time_master(func):
    print('开始运行')
    start=time.time()#获取时间戳
    func()
    stop=time.time()
    print('运行结束')
    print(f'一共耗费{(stop-start):.2f}秒')
def myfunc():
    time.sleep(2)
    print('hello lianhua')
time_master(myfunc)
```

### 2.优化：装饰器

```python
import time
def time_master(func):
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
def myfunc():
    time.sleep(2)
    print('I love lianhua')

#装饰器原本的样子
myfunc=time_master(myfunc)
myfunc()
```

@语法糖

```python
import time
def time_master(func):
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
@time_master
def myfunc():
    time.sleep(2)
    print('I love lianhua')
```

一个函数可以有多个装饰器修饰

执行顺序：从下往上

如何给装饰器传递参数？多加一次嵌套

```python
import time

def logger(msg):
    def time_master(func):
        def call_func():
            print('开始运行')
            start=time.time()
            func()
            stop=time.time()
            print('运行结束')
            print(f'一共耗费{(stop-start):.2f}秒')
        return call_func
    return time_master


#@logger(msg="A")
def funA():
    time.sleep(1)
    print('正在调用funA')


#@logger(msg="B")
def funB():
    time.sleep(1)
    print('正在调用funB')
#原本的样子
funA=logger(msg='A')(funA)
funB=logger(msg='B')(funB)
funA()
funB()
```

## 46.函数（7）

lambda(匿名函数)，一般处理简单的工作

```
lambda arg1,arg2,……，argn:expression

def<lambda>(arg1,arg2,……，argn):
	return expression
```

```python
#普通函数
def squarex(x):
    return x*x
squarex(3)#函数的引用squarex

#lambda
squarey=lambda y:y*y#函数引用squarey
squarey(3)

#但是，lambda是一个表达式
y=[lambda x:x*x,2,3]
y[0](y[1])#4
y[0](y[2])#9

mapped=map(lambda x:ord(x)+10,'lianhua')
list(mapped)

def boring(x):
    return ord(x)+10
list(map(boring,'lianhua'))

list(filter(lambda x:x%2,range(10)))

```

## 47.函数（8)

### 1.yied代替return

生成器

```python
def counter():#此时counter（）是一个生成器,每次调用提供一个数据
    i=0
    while i<=5:
        yield i#每次执行生成一个数据，暂停保留状态
        i+=1#下次调用从这里开始执行
#使用
for i in counter():
    print(i)
```

可以看出特殊的迭代器（支持next，不走回头路）

不支持下标索引

```python
c=counter()
next(c)#0
next(c)#1
next(c)#2
next(c)#3
next(c)#4
next(c)#5
next(c)#报错
```

```python
###求斐波那契数列
def fib():
    back1,back2=0,1
    while True:
        yield back1
        back1,back2=back2,back2+back1
f=fib()
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
```

### 2.生成器表达式

```
t=(i**2 for i in range(10))
next(t)
next(t)
next(t)
next(t)
for i in t:
    print(i)
```

![QQ_1739352994995](pytohn学习.assets/QQ_1739352994995.png)

## 48.函数（9）

递归

```python
def func(i):
    if i>0:
        print('lianhua')
        i-=1
        func(i)
func(3)
```

```python
###阶乘
#迭代
def fac(n):
    res=1
    for i in range(1,n+1):
        res=i*res
    return res
n=int(input('请输入一个数：'))
p=fac(n)
print(f'{n}的阶乘是{p}')

#递归
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
    
n=int(input('请输入一个数：'))
p=fac(n)
print(f'{n}的阶乘是{p}')
```

```python
###斐波那契数列
#迭代
def fac(n):
    a=1
    b=1
    c=1
    while n>2:
        c=a+b
        a=b
        b=c
        n-=1
    return c
fac(12)

#递归
def fac(n):
    if n==1 or n==2:
        return 1
    else:
        return fac(n-1)+fac(n-2)
print(fac(12))
```

## 49.函数（10）

```python
def move(n,x,y,z):
    if n==1:
        print(x,'->',z)
    else:
        move(n-1,x,z,y)
        print(x,'->',z)
        move(n-1,y,x,z)
n=int(input('请输入汉诺塔层数：'))
move(n,'A','B','C')
        
```



## 50.函数（11）

### 1.函数文档

help()

创建函数文档

```
def exchange(dollar,rate=6.32):
    '''功能：汇率转换，美元->人民币
    参数：
    -dollar 美元数量
    -rate 汇率
    返回值：
    -人民币的数量
    '''
    return dollar*rate

print(help(exchange))
```

![QQ_1739369322195](pytohn学习.assets/QQ_1739369322195.png)

### 2.类型注释

```
def times(s:str='fishc',n:int=3)->str:#类型，默认参数
    return s*n
times('lianhua',5)
times(5,5)

def timed(s:list[int],n:int=3)->list:
    return s*n

def timed(s:dict[str,int],n:int=3)->list:
    return list(s.keys())*n
```

要python做检测，用Mypy

### 3.内省

```
times.__name__#name获取函数名字
times.__annotations__#以字典类型打印函数里的三个类型注释
exchange.__doc__#查看函数文档
```

## 51.函数（12）

高阶函数

### 1.functools模块

reduce

```
def add(x,y):
    return x+y
import functools
a=functools.reduce(add,[1,2,3,4,5])
print(a)
#add(add(add(add(1,2),3),4),5)

b=functools.reduce(lambda x,y:x*y,range(1,11))
print(b)
```

### 2.偏函数

对指定函数进行二次包装

将一个函数的多个参数拆分多次进行传递

```
#与闭包类似
square=functools.partial(pow,exp=2)
square(2)
square(3)
cube=functools.partial(pow,exp=3)
cube(3)
```

![QQ_1739370736775](pytohn学习.assets/QQ_1739370736775.png)

### 3.@wraps

用来装饰装饰器的装饰器

引入：

```
import time
def time_master(func):
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
@time_master
def myfunc():
    time.sleep(2)
    print('I love lianhua')
print(myfunc.__name__)#装饰器的副作用
```

![QQ_1739398140094](pytohn学习

.assets/QQ_1739398140094.png)

```
import time
import functools
def time_master(func):
    @functools.wraps(func)#正真的函数是func传入的
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
@time_master
def myfunc():
    time.sleep(2)
    print('I love lianhua')
```

![QQ_1739398316416](pytohn学习.assets/QQ_1739398316416.png)

个人对其优化（使用闭包而不是语法糖）

```python
import time
import functools
def time_master(func):
    def call_func():
        print('开始运行')
        start=time.time()
        func()
        stop=time.time()
        print('运行结束')
        print(f'一共耗费{(stop-start):.2f}秒')
    return call_func
def myfunc():
    time.sleep(2)
    print('I love lianhua')
p=time_master(myfunc)
p()#调用call_func函数
print(myfunc.__name__)#装饰器的副作用
print(p.__name__)#装饰器的副作用
```

![QQ_1739398472773](pytohn学习.assets/QQ_1739398472773.png)

## 52.永久储存（上）如何操作文件

ctrl+s保存数据（保存在硬盘）

内存不能断电

创建并打开文件

open()

```python
f=open('lianhua.txt','w')#文件名，写入,返回文件对象
f.write('i love python')
f.writelines(['i love lianhua.\n','i love you'])
f.close()#保存
```

![QQ_1739399139960](pytohn学习.assets/QQ_1739399139960.png)

```python
f=open('lianhua.txt','w')#文件名，写入,返回文件对象
f.write('i love python')
f.writelines(['i love lianhua.\n','i love you'])
f.close()#保存

f=open('lianhua.txt','r+')#文件名，写入,重新打开，以r+的模式，更新文件,可读取可写入
#判断
print(f.writable())
print(f.writable())
for each in f:
    print(each)#指向文件末尾
print(f.tell())#追踪指针
print(f.read())#啥都没有，文件内部有文件指针，负责指向文件的当前位置，当在文件中读取一个字符的时候，这个文件指针会指向下一个字符，直到文件EOF
f.seek(0)
print(f.readline())
print(f.read())
f.write('i love my wife')
f.flush()#不关闭文件将内容保存到文件
f.truncate(29)#截断操作
f.close()
f=open('lianhua.txt','w')#也会发生截断
f.close ()
```

## 53.永久储存（中）如何处理路径

/

原始字符

### 1.查询路径

python3.4以后模块pathlib

```
from pathlib import Path#这种导入后面不加入模块名
p=Path.cwd()#获取文件当前目录
print(p)
```

![QQ_1739400360356](pytohn学习.assets/QQ_1739400360356.png)

```
#路径拼接
q=p/'lianhua.txt'
p.is_dir()
q.is_dir()
p.is_file()
q.is_file()
p.exists()
q.exists()
Path('C/404').exists()
p.name
q.name
q.stem
p.parent
q.suffix
ps=p.parents
for each in ps:
    print(each)
ps[0]#剪掉一节
ps[1]
p.parts
p.stat().st_size
p.stat()
```



#### 相对路径和绝对路径

```
Path('./doc')#相对路径，当前路径下doc这个文件夹
Path('../lianhua')#上一级路径
Path('./doc').resolve()#相对变绝对
p.iterdir()#获取当前路径下所有的子文件和子文件夹,得到一个生成器
for each in p.iterdir():
    print(each)
[x for x in p.iterdir() if x.is_file]
```

### 2.修改路径

```
from pathlib import Path#这种导入后面不加入模块名
p=Path.cwd()#获取文件当前目录
n=p/'FishC'
n.mkdir(exist_ok=True)#创建文件夹
n=p/'FisnC/A/B/C'
n.mkdir(parents=True,exist_ok=True)#创建文件夹,同时创建父级文件夹
n=n/"FisnC.txt"
f=n.open('w')
f.write('I love lianhua')
f.close()

#文件重命名
n.rename('newfishc.txt')#附带移动功能
m=Path('newfishc.txt')
m.replace(n)#文件替换

#删除
n.unlink()
n.parent.rmdir()

#查找
p=Path('.')
p.glob('*.txt')
print(list(p.glob('*.txt')))
list(p.glob('*/*.py'))
list(p.glob('**/*.py'))#向下递归搜索
```

## 54.永久储存（下）

### 1.上下文管理器

```
f=open('FishC.txt','w')
f.write('I love FishC.')
1/0#打断语句，未写入硬盘
f.close()


with open('FishC.txt.','w') as f:
    f.write('I love FishC')
    1/0#同样报错，但是with会帮我关闭
```

### 2.将python对象序列化

```
import pickle

x,y,z=1,2,3
s='lianhua'
l=['莲华',520,3.14]
d={'one':1,'two':2}

with open('data.pk1','wb') as f:
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(z,f)
    pickle.dump(s,f)
    pickle.dump(l,f)
    pickle.dump(d,f)
```

```
###把鸟文读回来
import pickle
with open('data.pk1','rb') as f:
    x=pickle.load(f)
    y=pickle.load(f)
    z=pickle.load(f)
    s=pickle.load(f)
    l=pickle.load(f)
    d=pickle.load(f)
print(x,y,z,s,l,d,sep='\n')
```

![QQ_1739422024202](pytohn学习.assets/QQ_1739422024202.png)

```python
#改进
import pickle
with open('data.pk1','rb') as f:
    x,y,z,s,l,d=pickle.load(f)#解包

print(x,y,z,s,l,d,sep='\n')
```

## 55.异常（上）

### 1.语法错误

```
’lianhua'+520
```

看不懂？去查内置异常

### 2.处理异常

try:

检查范围

except[expression [as identier]]:

 异常处理代码

```python
try:
    1/0
except ZeroDivisionError as e:#精确定位
    print(e)

```

```python
try:
    1/0
    520+'lianhua'
except (ZeroDivisionError,ValueError,TypeError):
    pass
```

```python
try:
    1/0
    520+'lianhua'#会被忽略
except ZeroDivisionError:
    print('除数不能0')
except ValueError:
    print('值不正确')
except TypeError:
    print('类型不正确')
```

![QQ_1739422958470](pytohn学习.assets/QQ_1739422958470.png)

## 56.异常（下）

### 1.

```python
try:
    1/0
except:
    print('逮到了')
else:
    print('没逮到')
finally:
    print('逮没逮到都会执行')


try:
    f=open('fishc.txt','w')
except:
    print('出错了')
finally:
    f.close()
 
 
try:
    while True:
        pass
finally:
    print('晚安')
```



异常的嵌套

```python
try:
    try:
        520+'lianhua'
    except:
        print('内部异常')
    1/0
except:
    print('外部异常')
finally:
    print('收尾工作')
```

### 2.raise

主动引发异常

```
raise ValueError('值不正确')
#不能用raise生成不存在的异常
```

```
try:
    1/0
except:
    raise ValueError('这样不行')#偷天换日

#异常链
raise ValueError('这样可不行') from ZeroDivisionError
```

### 3.assert

主动引发异常，调试代码

![QQ_1739429492628](pytohn学习.assets/QQ_1739429492628.png)

直接抛出异常，省去if语句

### 4.利用异常实现goto

```python
try:
    while True:
        while True:
            for i in range(10):
                if i>3:
                    raise
                print(i)
            print('被跳过')
        print('被跳过')
    print('被跳过')
except:
    print('到这儿来了')
```

![QQ_1739430019305](pytohn学习.assets/QQ_1739430019305.png)

## 57.类和对象（1）封装

面向对象是一种代码封装的方法

对象=属性+方法

class->

```python
class Turtle:#用大写字母开头（约定俗成）
    head=1
    eyes=2
    legs=4
    shell=True

    def run(self):
        print('虽然我行动慢，但遇到危险也会狂奔')
    def crawl(self):
        print('不积跬步无以至千里')
    def bite(self):
        print('我会咬人')
    def sleep(self):
        print('ZZZ')
    def eat(self):
        print('谁知盘中餐，粒粒皆辛苦')
t1=Turtle()
print(t1.head)
t1.sleep()
t2=Turtle()
#修改
t2.legs=3
print(t1.legs)
print(t2.legs)
#添加属性
t1.mouth=1
print(dir(t1))
print(dir(t2))

```

对象无处不在

```
x=520
type(x)
y='lianhua'
type(y)
```

self让python知道是哪个对象在调用

```python
class C:
    def get_self(self):
        print(self)
c=C()
c.get_self()#打印实例对象本身
#C.get_seif(c)
```

## 58.类和对象（2）继承

面向对象的编程的三大特点：封装，继承

### 1.继承

```python
class A:
    x=520
    def hello(self):
        print('hello,我是A')
class B(A):#子类
    pass
b=B()
b.x
b.hello()
class B(A):
    x=990#覆盖
    def hello(self):#覆盖
        print('你好，我是B')
b=B()
b.x
b.hello()


#判断一个对象是否属于某个类
isinstance(b,B)
isinstance(b,A)
#检测一个类是否为另一个类的子类
issubclass(A,B)
```

```python
class A:
    x=520
    def hello(self):
        print('hello,我是A')

class B:
    x=880
    y=250
    def hello(self):
        print('你好，我是C')
#多重继承
class C(A,B):
    pass
c=C()
c.x#520
c.hello()#A
#从左到右访问
c.y#250
```



### 2.组合

```python
class Turtle:
    def say(self):
        print('不积跬步无以至千里')
class Cat:
    def say(self):
        print('瞄')
class Dog:
    def say(self):
        print('汪汪汪')
class Garden:
    t=Turtle()
    c=Cat()
    d=Dog()
    def say(self):
        self.t.say()#加上self,绑定
        self.c.say()
        self.d.say()
g=Garden()
g.say()

```

## 59.类和对象（3)绑定

```python
class C:
    def get_self(self):
        print(self)
d=C()
c=C()
d.x=250
c.x=520
c.x#520
d.x#250
c.y=660
#内省
c.__dict__#{'x':520,'y':660}
```



```python
class C:
    def set_x(self,v):
        self.x=v

c=C()
c.__dict__#{}
c.set_x(250)
c.__dict__#{'x':250}

```

```python
class C:
    x=100
    def set_x(self,v):
        x=v
c=C()
c.set_x(250)#谁都改不了
c.x#100
C.x#100
C.x=250
c.x#250
c.__dict__#{}对象没有不代表类没有类没有不代表父类没有

```

### 一个旁门左道的小技巧

最小的类

```
class C:
    pass
#当字典使用
C.x=250
C.z=[1,2,3]
C.y='lianhua'
print(C.x)
print(C.z)
print(C.y)

#真正的字典
d={}
d['x']=250
d['y']='lianhua'
d['z']=[1,2,3]
print(d['x'])
print(d['y'])
print(d['z'])

#更常用的方式
class C:
     pass
c=C()
c.x=250
c.y='小甲鱼'
c.z=[1,2,3]
```

## 60.类和对象（4）

### 1.构造函数

`__init__` 方法用于初始化对象的属性，在创建实例时自动调用。

```python
#__init__()构造函数
class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
c=C(2,3)
c.add()#5
c.mul()#6
print(c.__dict__)
```

### 2.重写

```python
#__init__()
class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
c=C(2,3)
c.add()#5
c.mul()#6
print(c.__dict__)

#子类对父类的重写
class D(C):
    def __init__(self, x, y,z):
        C.__init__(self,x,y)
        self.z=z
    def add(self):
        return C.add(self)+self.z
    def mul(self):
        return C.mul(self)*self.z
d=D(2,3,4)
print(d.add())
print(d.mul())
#调用未绑定的父类的方法：直接通过类访问类里方法的做法
```

### 3.钻石继承

问题：

```python
class A:
    def __init__(self):
        print('hellp, 我是A')
class B1(A):
    def __init__(self):
        A.__init__(self)
        print('hello,我是B1')
class B2(A):
    def __init__(self):
        A.__init__(self)
        print('hello,我是B2')
class C(B1,B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print('hello，我是C')
c=C()#A被调用2次

```

解决：

super()自动避免重复，MRO顺序

```python
class A:
    def __init__(self):
        print('hello, 我是A')
class B1(A):
    def __init__(self):
        super().__init__()
        print('hello,我是B1')
class B2(A):
    def __init__(self):
        super().__init__()
        print('hello,我是B2')
class C(B1,B2):
    def __init__(self):
        super().__init__()
        print('hello，我是C')
c=C()

```

![QQ_1739447771714](pytohn学习.assets/QQ_1739447771714.png)

```
#查找类的MRO
#1.
C.mro()
B1.mro()
#2.
C.__mro__
B1.__mro__

```

## 61.类和对象（5）

Mixin

```python
class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print(f'我叫{self.name},今年{self.age}岁')

class Flymixin:
    def fly(self):
        print('我还会飞')

class pig(Flymixin,animal):
    def special(self):
        print('我的技能是拱大白菜')

p=pig('fishc',5)
p.say()
p.special()
p.fly()
```

![QQ_1739448605134](pytohn学习.assets/QQ_1739448605134.png)

### 实例分析

```python
class displayer:#第二步
    def display(self,message):
        print(message)

class loggerminxin:
    def log(self,messaage,filename='lodfile.txt'):
        with open(filename,'a') as f:
            f.write(messaage)

    def display(self,message):#第一步
        super().display(message)
        #去父类查找方法，没有，默认object。super依靠，MRO，这里去displayer
        #mysubclass.mro()
        #MRO 的顺序是：mysubclass → loggerminxin → displayer → object。
        self.log(message)#self其实是subclass

class mysubclass(loggerminxin,displayer):#先左后右，第三步
    def log(self,message):
        super().log(message,filename='subclasslog.txt')
        #MRO 的顺序是：mysubclass → loggerminxin → displayer → object。

subclass=mysubclass()#实例化一个个对象
subclass.display('This is a test.')

```

## 62.类和对象（6）多态

```
#运算符的多态
3+5
3*5
'py'+'lianhua'
'lianhua'*3

#函数的多态
len('lianhua')#字符个数
len(['lianhua','py','bjfu'])
len({'name':'lianhua','age':18})

```

```
#类继承的多态,重写
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass

class square(shape):
    def __init__(self, length):
        super().__init__('正方形')
        self.length=length
    def area(self):
        return self.length*self.length

class circlre(shape):
    def __init__(self, radius):
        super().__init__('圆形')
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

class triangle(shape):
    def __init__(self, base,height):
        super().__init__('三角形')
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height/2

s=square(5)
c=circlre(6)
t=triangle(3,4)
s.name
c.name
t.name
s.area()
c.area()
t.area()
```



自定义函数如何实现多接口？

```python
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只猫,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('miao')

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只狗,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('wow')

class pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'我是一只猪,我叫{self.name},今年{self.age}岁')
    def say(self):
        print('oink')

c=cat('web',4)
d=dog('fish',7)
p=pig('dada',5)

def animal(x):
    x.intro()
    x.say()

animal(c)
animal(d)


#鸭子类型
class byc:
    def intro(self):
        print('我曾经跨国三和大海')
    def say(self):
        print('都有自行车了,还要什么兰博基尼')

b=byc()
animal(b)
```

## 63.类和函数（7）

”私有变量“

name mangling

```
class C:
    def __init__(self,x):
        self.__x=x
    def set_x(self,x):
        self.__x=x
    def get_x(self):
        print(self.__x)
c=C(250)
#c.__x访问不到
c.get_x()
c.set_x(520)
c.get_x()
print(c.__dict__)
print(c._C__x)#私有变量实际是改了个名字

```

![QQ_1739475426447](pytohn学习.assets/QQ_1739475426447.png)



```
#方法名
class D:
    def __func(self):
        print('fishc')

d=D()
#d.__func()
d._D__func()
#添加私有变量？不行
#名字改编是发生在类实例化对象时
c.__y=250
```



\#  _变量仅供内部访问，不要去访问

\# 变量_



### 效率

字典是用空间换时间

```
class C:
    def __init__(self,x):
        self.x=x
c=C(250)
print(c.__dict__)
c.y=520
print(c.__dict__)
c.__dict__['z']=666
print(c.__dict__)
```

![QQ_1739475934937](pytohn学习.assets/QQ_1739475934937.png)

避免浪费：slots

```
class C:
    __slots__=['x','y']
    def __init__(self,x):
        self.x=x


c=C(250)
c.y=520
c.z=666#报错

```

![QQ_1739476320274](pytohn学习.assets/QQ_1739476320274.png)

继承自父类的slots属性不会在子类生效

```
class C:
    __slots__=['x','y']
    def __init__(self,x):
        self.x=x

class E(C):
    pass
e=E(520)
e.y=250
e.z=666
print('e.__slots__')#有属性，但不生效
print(e.__dict__)
```

![QQ_1739476948957](pytohn学习.assets/QQ_1739476948957.png)

![QQ_1739476964725](pytohn学习.assets/QQ_1739476964725.png)

![QQ_1739477004228](pytohn学习.assets/QQ_1739477004228.png)

## 64.类和对象（8）魔法方法

### 1.对象的构造

![QQ_1739477618496](pytohn学习.assets/QQ_1739477618496.png)



![QQ_1739478051788](pytohn学习.assets/QQ_1739478051788.png)



![QQ_1739478080799](pytohn学习.assets/QQ_1739478080799.png)



![QQ_1739478181060](pytohn学习.assets/QQ_1739478181060.png)



```python
#__init__
#对象诞生先调用__new__(cls[,…])创建类的实例，返回对象self,再传递给__init__()
class caps(str):
    def __new__(cls,string):
        string=string.upper()
        return super().__new__(cls,string)# 调用父类 str 的 __new__ 方法创建字符串实例



cs=caps('Fishc')
print(cs)
print(cs.lower())#继承str
print(cs.capitalize())
```



![QQ_1739478273425](pytohn学习.assets/QQ_1739478273425.png)

### 2.对象的销毁

```python
class C:
    def __init__(self):
        print('我来了')
    def __del__(self):
        print('我走了')

c=C()
del c#对象被销毁才会调用魔法方法

c=C()
d=c#引用,被引用不会被销毁
del c
del d
```

### 3.对象的重生

把self送出去

```python
#函数调用
class E:
    def __init__(self,name,func):
        self.name=name
        self.func=func
    def __del__(self):
        self.func(self)

#闭包
def outter():
    x=0
    def inner(y=None):
        nonlocal x#用于在嵌套函数中声明变量为外层函数的局部变量，使得内层函数可以修改外层函数的变量。 

        if y:
            x=y
        else:
            return x#窃取self
    return inner

f=outter()#调用 outter，返回 inner 函数，并将其赋值给变量 f。此时，f 是一个闭包，封闭了 outter 中的变量 x。
e=E('lianhua',f)
print(e)
e.name
del e
g=f()#就是e
print(g.name)
```

## 65.类和方法（9）有关运算的魔法方法（上）

```python
#加法

class S(str):
    def __add__(self,other):
        return len(self)+len(other)
s1=S('lianhua')
s2=S('python')
print(s1+s2)#s1+s2即s1.__add__(s2)
print(s1+'python')
print('python'+s2)
```



调用前提：1.两个对象不同类

2.左侧未定义或返回NotImplemented

```python
#反算术运算加法
class s1(str):
    def __add__(self,other):
        return NotImplemented#表示魔法方法未实现
#p1必须不能实现add,不然优先用左侧
class s2(str):
    def __radd__(self,other):
        #不能写成add，矛盾
        return len(self)+len(other)
p1=s1('banaba')
p2=s2('apple')
print(p1+p2)
```

```python
#增强赋值运算,运算加赋值
#p1+=p2即p1=p1.__iadd__(s2),会修改对象自身
class s1(str):
    def __iadd__(self,other):
        return len(self)+len(other)

class s2(str):
    def __radd__(self,other):
        return len(self)+len(other)
p1=s1('apple')
p2=s2('banana')
p1+=p2
print(p1)
print(type(p1))#class被改为int


#如果增强运算符没实现左侧的魔法方法，则使用add 或者 radd
p2+=p2 #p2 p2同类，去str查找add
print(p2)
print(type(p2))
```



```python
#int（self）拦截魔法方法,只要一个参数
#将中文转化成整数
class myint:
    def __init__(self,num):
        self.num=num
    
    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh={'零':0,'一':1,'二':2,'三':3,'四':4,
            '五':5,'六':6,'七':7,'八':8,'九':9}
            result=0
        for each in self.num:
            if each in zh:
                result+=zh[each]
            else:
                result+=int(each)
            result*=10

        return result//10
n=myint('五二零1413')
print(n)#print(n) 打印的是 n 这个对象本身，而不是它的整数值

#在 Python 中，当你打印一个对象（像 n 这样的自定义类对象）时，
# 默认情况下，它不会直接显示对象的内容，而是显示它的内存地址，
# 比如 <__main__.myint object at 0x...>。
# 如果你想让打印出来的内容更有意义（比如数字），
# 你需要告诉 Python 如何显示这个对象的内容
print(int(n))


print(int(3.14))

```

## 66.类和对象（10）运算有关的魔法方法（下）

and 

or 

not

按位与或非（对两个整数）

```python
print(3&4)
print(bin(2))#获取二进制
print(3|4)
print(~3)#补码011 100
print(3^2)
```

<< >>

```
#运算对象<<移动位数(不能是负数)
bin(8)#10000
8>>2#10  8//pow(2,2)
8>>3#8//pow(2,3)  一定用地板除，因为移位会丢失数据
8<<2#100000 8*pow(2,2)

```

优先级：递增| ^ &

~-+同意优先级



```
#math模块
import math
print(0.1+0.2==0.3+math.ulp)#3.9版本，打印Ture
```

![QQ_1739517744859](pytohn学习.assets/QQ_1739517744859.png)

```
#易错，让对象作为索引值才会触发
class C:
    def __index__(self):
        print('被拦截了')
        return 3
c=C()
s='lianhua'
# s[c]
print(s[c])
bin(c)
print(bin(c))

```

## 67.类和对象（11）属性访问的魔法方法

```
#函数
class C:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

c=C('lianhua',18)
print(hasattr(c,'name'))
print(getattr(c,'name'))
print(getattr(c,'_C__age'))
print(setattr(c,'_C__age',19))
print(getattr(c,'_C__age'))
delattr(c,'_C__age')
print(hasattr(c,'_C__age_'))
```

魔法方法

### 1.

```
class C:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def __getattribute__(self, attrname):
        print('拿来吧你')
        return super().__getattribute__(attrname)
        #在方法内部，首先打印 '拿来吧你'，
        # 然后使用 super().__getattribute__(attrname) 调用父类的 __getattribute__ 方法，
        # 获取属性的实际值。
c=C('lianhua',18)
print(getattr(c,'name'))
print(c._C__age)
c.fishc

```

![img](pytohn学习.assets/{67075ADF-81DD-445C-BCB2-EA54E207E0C0})

![QQ_1739519202569](pytohn学习.assets/QQ_1739519202569.png)

### 2.

```python
class C:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def __getattribute__(self, attrname):
        print('拿来吧你')
        return super().__getattribute__(attrname)
        #在方法内部，首先打印 '拿来吧你'，
        # 然后使用 super().__getattribute__(attrname) 调用父类的 __getattribute__ 方法，
        # 获取属性的实际值。
    def __getattr__(self,attrname):#当用户试图获取不存在的属性触发
        if attrname=='lianhua':
            print(' i love lianhua')
        else:
            raise ArithmeticError(attrname)

        
c=C('lianhua',18)
print(getattr(c,'name'))
print(c.lianhua)
```

![QQ_1739533676789](pytohn学习.assets/QQ_1739533676789.png)

![QQ_1739533710766](pytohn学习.assets/QQ_1739533710766.png)

![QQ_1739533719760](pytohn学习.assets/QQ_1739533719760.png)

死亡螺旋

```python
#无限递归
class D:
    def __setattr__(self, name, value):
        self.name=value
#在您提供的代码中，
# 类 D 定义了 __setattr__ 方法，
# 用于拦截对实例属性的赋值操作。 
# 当您创建 D 类的实例 d 并尝试设置 d.name = 'lianhua' 时，
# __setattr__ 方法会被调用。
#  然而，在 __setattr__ 方法内部，
# 您直接使用 self.name = value 来设置属性值，
# 这会再次触发 __setattr__ 方法，导致无限递归调用，
# 最终引发 RecursionError。
d=D()
d.name='lianhua'
```

```python
class D:
    def __setattr__(self, name, value):
        self.__dict__[name]=value
d=D()
d.name='lianhua'
```



```
class D:
    def __setattr__(self, name, value):
        self.__dict__[name]=value
    def __delattr__(self, name):
        del self.__dict__[name]
d=D()
d.name='lianhua'
print(d.__dict__)
del d.name
print(d.__dict__)
```

![QQ_1739534460894](pytohn学习.assets/QQ_1739534460894.png)



## 68.类和对象（12）

### 1.索引

```python
class C:
    def __getitem__(self,index):
        print(index)
c=C()
c[2]#2
c[2:8]#slice(2,8,None),bif函数，切片是它的语法糖
s='I love fishc'
s[2:6]#'love
s[slice(2,6)]#'love
s[7:]#'fishc
s[slice(7,None)]#'fishc
s[::4]#'Ivi
s[slice(None,None,4)]
```

```python
#为索引或切片赋值会被__setitem__()拦截
class D:
    def __init__(self,data):
        self.data=data
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self,index,value):
        self.data[index]=value 
d = D([1, 2, 3,4,5])
print(d[0])  # 输出 1（调用 __getitem__）
d[1] = 1
print(d.data)  
d[2:4]=[2,3]
d[:]#[1,1,2,3,5]
```

![QQ_1739547317043](pytohn学习.assets/QQ_1739547317043.png)

```python
#与获取相关的操作也会被拦截
class D:
    def __init__(self,data):
        self.data=data
    def __getitem__(self,index):
        return self.data[index]*2
d=D([1,2,3,4,5])
for i in d:
    print(i,end=' ')
```



![QQ_1739547711368](pytohn学习.assets/QQ_1739547711368.png)

```
#__iter__(self)  __next__(self)
#模拟for的执行流程
x=[1,1,2,3,5]
_=iter(x)
while True:
    try:
        i=_.__next__()
    except StopIteration:
        break
    print(i,end=' ')
```

![QQ_1739550917384](pytohn学习.assets/QQ_1739550917384.png)

用于**将可迭代对象转换为迭代器**

![QQ_1739551067693](pytohn学习.assets/QQ_1739551067693.png)

```
#自己创建迭代器对象
class double:
    def __init__(self,start,stop):
        self.value=start-1
        self.stop=stop
    def __iter__(self):
        return self# 关键：返回自身，说明实例是迭代器
    def __next__(self):
        if self.value==self.stop:
            raise StopIteration
        self.value+=1
        return self.value*2
d=double(1,5)
for i in d:
    print(i,end=' ')
```



![QQ_1739550302996](pytohn学习.assets/QQ_1739550302996.png)



## 69.类和对象（13）代偿

### 1.contains

```
#__contains__(self)

class C:
    def __init__(self,data):
        self.data=data
    def __contains__(self,item):
        print('hi')
        return item in self.data
c=C([1,2,3,4,5])
print(3 in c)
```

![QQ_1739551473826](pytohn学习.assets/QQ_1739551473826.png)

==没有contains，去找iter 和next,再不济，找getitem==

```
class C:
    def __init__(self,data):
        self.data=data
    def __iter__(self):
        print('iter',end='->')
        self.i=0
        return self
    def __next__(self):
        print('next',end='->')
        if self.i==len(self.data):
            raise StopIteration
        item=self.data[self.i]
        self.i+=1
        return item

c=C([1,2,3,4,5])
print(3 in c)
print(6 in c)
```

```
class C:
    def __init__(self,data):
        self.data=data
    def __getitem__(self,index):
        print('getitem',end='->')
        return self.data[index]

c=C([1,2,3,4,5])
print(3 in c)
print(6 in c)
```

![img](pytohn学习.assets/{C22E7FBE-194B-4FFD-A8CF-7F9C9AEF7AE9})

### 2.bool

找不到bool 找len

```
class D:
    def __bool__(self):
        print('bool')
        return True
d=D()
print(bool(d))
```

![QQ_1739552600981](pytohn学习.assets/QQ_1739552600981.png)



```
class D:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        print('len')
        return len(self.data)#Ture为非零
d=D('lianhua')
print(bool(d))
```

![QQ_1739552721380](pytohn学习.assets/QQ_1739552721380.png)



### 3.比较运算符的魔法方法

```
class S(str):
    def __lt__(self,other):
        return len(self)<len(other)
    def __gt__(self,other):
        return len(self)>len(other)
    def __eq__(self,other):
        return len(self)==len(other)
    __le__=None#这里不加这个的话，还是比较编码，加了出现不合适的关系会报错
    __ge__=None
    __ne__=None

s=S('lianhua')
p=S('Lianhua')
print(s==p)

```

类似地，如果

```
__contains__=None
```

代偿也不能实现

```
class C:
    def __init__(self,data):
        self.data=data
    def __iter__(self):
        print('iter',end='->')
        self.i=0
        return self
    def __next__(self):
        print('next',end='->')
        if self.i==len(self.data):
            raise StopIteration
        item=self.data[self.i]
        self.i+=1
        return item
    __contains__=None

c=C([1,2,3,4,5])
print(3 in c)

```

## 70.类和对象（14）对象调用的相关魔法方法

```
#__call_-(self[,args])
class C:
    def __call__(self,*args,**kwargs):
        print(f'位置参数{args}\n关键字参数{kwargs}')
c=C()
c(1,2,3,x=4,y=5)
```

![QQ_1739553642541](pytohn学习.assets/QQ_1739553642541.png)

```
class power:
    def __init__(self,exp):
        self.exp=exp
    def __call__(self,base):
        return base**self.exp
square=power(2)
cube=power(3)
print(square(3))
```

和字符串相关的魔法方法

了解函数

```
#__str__(self) __repr__(self)
#str给人看的   repr给机器就看的
str(520)#520
repr(520)#520
str('lianhua')#'lianhua'
repr('lianhua')#'"lianhua"'多义词引号
#eval去引号后执行，相当于repr的反函数
eval(str('lianhua'))#报错
eval(repr('lianhua'))#lianhua
eval(repr(520))#520
```

```
#repr可以代仓str
class C:
    def __repr__(self):
        return 'I love lainhua'
c=C()
print(str(c))
print(repr(c))#repr(c)

#str只用于对象出现在打印操作的顶层
#repr场景更多
cs=[C(),C(),C()]
for each in cs:
    print(each)
print(cs)
```

![QQ_1739581775432](pytohn学习.assets/QQ_1739581775432.png)

```
class C:
    def __str__(self):
        return 'I love lainhua'
c=C()
print(str(c))
print(repr(c))#repr(c)得到<__main__

#str只用于对象出现在打印操作的顶层
#repr场景更多
cs=[C(),C(),C()]
for each in cs:
    print(each)
print(cs)
```

![QQ_1739581814607](pytohn学习.assets/QQ_1739581814607.png)

```python
class C:
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return f'data={self.data}'
    def __repr__(self):
        return f'C{self.data}'
    def __add__(self,other):
        self.data+=other

c=C(250)
print(c)#data=250
c#C(250)
c+250
print(c)#data=500
c#C(500)
print(C(39))#data=39
```

## 71.类和对象（15）property

class property(fget=None,fset=None,fdel=None,doc=None)

返回property属性对象

![QQ_1739586342983](pytohn学习.assets/QQ_1739586342983.png)

```
class C:
    def __init__(self):
        self._x=250#隐藏使用
    def getx(self):
        return self._x
    def setx(self,value):
        self._x=value
    def delx(self):
        del self._x
    x=property(getx,setx,delx)
#     属性绑定
# 使用 property() 函数将 getx、setx、delx 分别绑定到属性 x 的读取、写入和删除操作。
# 此时，x 成为一个“托管属性”，所有对 x 的操作都会通过对应的方法间接操作 _x。

c=C()
print(c.x)
c.x=520
print(c.__dict__)
del c.x
print(c.__dict__)

```

用getarrr等实现上述代码

```
class D:
    def __init__(self):
        self._x=250
    def __getattr__(self,name):
        if name=='x':
            return self._x
        else:
            super().__getattr__(name)
    def __setattr__(self,name,value):
        if name=='x':
            super().__setattr__('_x',value)
        else:
            super().__setattr__(name,value)
    def __delattr__(self,name):
        if name=='x':
            super().__delattr__('_x')
        else:
            super().__delattr__(name)

d=D()
print(d.x)
d.x=520
print(d.__dict__)
del d._x
print(d.__dict__)

```

![QQ_1739587736148](pytohn学习.assets/QQ_1739587736148.png)

装饰器

```
class E:
    def __init__(self):
        self._x=250
    @property
    def x(self):
        return self._x

class E:
    def __init__(self):
        self._x=250
    def x(self):
        return self._x
    x=property(x)
```

但是不能修改和删除

改进

```
class E:
    def __init__(self):
        self._x=250
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @x.deleter
    def x(self):
        del self._x
e=E()
print(e.x)
e.x=520
print(e.__dict__)
del e.x
print(e.__dict__)
```

![](pytohn学习.assets/QQ_1739604052565.png)

![QQ_1739604068886](pytohn学习.assets/QQ_1739604068886.png)

## 72.类和对象（16）类方法和静态方法

类的方法类不能类自己调用，方法需要对象来绑定

### 1.类方法

@classmethod不需要对象绑定

```
class C:
    def funa(self):
        print(self)
    @classmethod
    def funb(cls):
        print(cls)
c=C()
c.funa()#绑定对象
c.funb()#绑定C
```

在Python中，**实例属性**和**类属性**是两种不同的属性类型，它们的定义、作用域和用途各有不同。以下是详细解释和示例：

---

#### **1. 实例属性**

- **定义**：实例属性属于类的具体实例（对象），每个实例拥有独立的属性副本。
- **声明方式**：通常在类的`__init__`方法中通过`self.属性名`定义。
- **特点**：
  - 每个实例的属性可以不同。
  - 实例属性的修改仅影响当前实例。

#### **示例**：
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

# 创建两个实例
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # 输出: Buddy（实例属性）
print(dog2.age)   # 输出: 5（实例属性）
```

---

#### **2. 类属性**

- **定义**：类属性属于类本身，所有实例共享该属性。
- **声明方式**：直接在类作用域中定义（不在任何方法内）。
- **特点**：
  - 所有实例共享同一个类属性。
  - 修改类属性会影响所有实例（除非实例覆盖了该属性）。

##### **示例**：

```python
class Dog:
    species = "Canine"  # 类属性（所有狗的物种）

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 所有实例共享类属性
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.species)  # 输出: Canine
print(dog2.species)  # 输出: Canine

# 修改类属性（通过类名）
Dog.species = "Feline"
print(dog1.species)  # 输出: Feline（所有实例的类属性被修改）
print(dog2.species)  # 输出: Feline

# 通过实例修改同名属性会创建实例属性
dog1.species = "Canine"
print(dog1.species)  # 输出: Canine（实例属性覆盖类属性）
print(dog2.species)  # 输出: Feline（类属性未被修改）
```

---

#### **3. 关键区别**

| **特性**     | **实例属性**               | **类属性**                 |
| ------------ | -------------------------- | -------------------------- |
| **作用域**   | 属于实例                   | 属于类                     |
| **存储位置** | 每个实例独立存储           | 类中统一存储               |
| **修改影响** | 仅影响当前实例             | 影响所有实例（除非被覆盖） |
| **声明位置** | `__init__`方法内通过`self` | 类作用域直接定义           |

---

#### **4. 实际应用场景**

- **实例属性**：用于描述对象特有的状态（如人的姓名、年龄）。
- **类属性**：用于描述类的公共特征或共享数据（如默认配置、计数器）。

##### **示例：类属性实现计数器**

```python
class Counter:
    count = 0  # 类属性（统计实例数量）

    def __init__(self):
        Counter.count += 1  # 每次创建实例时递增

c1 = Counter()
print(c1.count)  # 输出: 1

c2 = Counter()
print(c2.count)  # 输出: 2

print(Counter.count)  # 输出: 2（直接通过类访问）
```

---

#### **5. 注意事项**

- **避免通过实例修改类属性**：  
  如果通过实例修改类属性（如`obj.class_attr = value`），会创建同名的实例属性，覆盖类属性，导致后续访问该实例属性时不再引用类属性。
- **优先使用类名操作类属性**：  
  若需修改类属性，应通过类名直接操作（如`ClassName.class_attr = value`）。

---

通过理解实例属性和类属性的区别，可以更灵活地设计类的结构和行为。



```
class C:
    count=0
    def __init__(self):
        C.count+=1
    @classmethod
    def getc(cls):
        print(f'该类一共实例化了{cls.count}个实例对象')
c1=C()
c2=C()
c3=C()
c3.getc()
c3.count=1
#一般来说，实例属性和类属性同名时，实例属性会覆盖类属性
#但是这里是类方法，影响不大
print(c3.count)
c3.getc()
```

![QQ_1739605413621](pytohn学习.assets/QQ_1739605413621.png)

### 2.静态方法

在类里定义不需要绑定对象的函数

```
class C:
    @staticmethod
    def func():
        print('i love lianhua')
c=C()
c.func()
C.func()
```

```
class C:
    count=0
    def __init__(self):
        C.count+=1
    @staticmethod
    def getc():
        print(f'该类一共实力化了{C.count}个对象')#拿不到类直接.C
c1=C()
c2=C()
c3=C()
c3.getc()
```

不用担心对象覆盖属性问题，直接C.count

```python
class C:
    count=0
    @classmethod
    def add(cls):
        cls.count+=1
    def __init__(self):
        self.add()
    @classmethod
    def getc(cls):
        print(f'该类一共实例化了{cls.count}个实例对象')
class D(C):
    count=0
class E(C):
    count=0
c1=C()
d1,d2=D(),D()
e1,e2,e3=E(),E(),E()
c1.getc()
d1.getc()
e1.getc()
```

![QQ_1739606926122](pytohn学习.assets/QQ_1739606926122.png)

### **3.总结对比表**

| 特性             | 类方法（`@classmethod`）       | 静态方法（`@staticmethod`） |
| :--------------- | :----------------------------- | :-------------------------- |
| **第一个参数**   | `cls`（类本身）                | 无特殊参数                  |
| **访问类属性**   | ✅ 通过 `cls`                   | ❌ 不能直接访问              |
| **访问实例属性** | ❌（除非通过实例）              | ❌                           |
| **用途**         | 工厂方法、操作类状态、多态设计 | 工具函数、代码组织          |
| **继承时的行为** | 自动指向子类                   | 保持父类逻辑                |

------

### **何时使用？**

- **用类方法**：需要访问类状态、实现多态构造函数，或在继承中自适应子类。

- **用静态方法**：方法逻辑独立于类和实例，纯粹作为工具函数存在。

	

## 73.类和对象（17）描述符

![QQ_1739667924418](pytohn学习.assets/QQ_1739667924418.png)

```python
class D:
    def __get__(self,instance,owner):#x,D()   c    C
        print(f'get\nself->{self}\nintstance->{instance}\nowner->{owner}')
    def __set__(self,instance,value):
        print(f'set\nself->{self}\nintstance->{instance}\nvalue->{value}')
    def __delete__(self,instance):
        print(f'delete\nself->{self}\ninstance->{instance}')
class C:
    x=D()
c=C()
c.x=250
c.x
del c.x
```

![QQ_1739675569869](pytohn学习.assets/QQ_1739675569869.png)

模拟实现property

```python
class D:
    def __get__(self,instance,owner):
        return instance._x
    def __set__(self,instance,value):
        instance._x=value
    def __delete__(self,instance):
        del instance._x
class C:
    def __init__(self,x=250):
        self._x=x
    x=D()
    
c=C()
print(c.x)
c.x=520
print(c.__dict__)
del c.x
print(c.__dict__)
```

```python
class myproperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)#c
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x=250
    def getx(self):
        return self._x
    def setx(self,value):
        self._x=value
    def delx(self):
        del self._x
    x=myproperty(getx,setx,delx)
c=C()
print(c.x)
c.x=520
print(c.__dict__)
del c.x
print(c.__dict__)

```

当装饰器

尝试实现getter(),settter(),deleter()

```python
class myproperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)
    def getter(self,func):
        self.fset=func
        return self
    def setter(self,func):
        self.fset=func
        return self
    def deleter(self,func):
        self.fdel=func
        return self

class D:
    def __init__(self):
        self._x=250
    @myproperty
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @x.deleter
    def x(self):
        del self._x
d=D()
print(d.x)
d.x=520
print(d.__dict__)
del d.x
print(d.__dict__)


```



```python
class myproperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)#c
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)
    def getter(self,func):
        self.fget=func
        return self
    def setter(self,func):
        self.fset=func
        return self
    def deleter(self,func):
        self.fdel=func
        return self
class E:
    def __init__(self):
        self._x=250
    x=myproperty()
    @x.getter
    def getx(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @x.deleter
    def x(self):
        del self._x
        e=E()
print(e.x)
e.x=520
print(e.__dict__)
del e.x
print(e.__dict__)
```

## 74.类和对象（18）描述符

==描述符只用于类属性==

属性访问优先级

数据描述符>实例对象属性>非数据描述符>类属性（MRO）

### 1.数据描述符

set delete

```
class D:
    def __get__(self,instance,owner):
        print('get')
    def __set__(self,instance,value):
        print('set')

class C:
    x=D()
c=C()
c.x
c.x='fish'
c.x
print(c.__dict__)
c.__dict__['x']='fishc'
print(c.__dict__)
c.x
```

![img](pytohn学习.assets/{0FD9A417-5BA5-49FE-A51C-70F1827409AF})

### 2.非数据描述符

get

```
class D:
    def __get__(self,instance,owner):
        print('get')
class C:
    x=D()
c=C()
c.x
c.x='fish'
c.x
```

![QQ_1739681566900](pytohn学习.assets/QQ_1739681566900.png)



### 3.

```
__set_name__(self,name,owner)
```

```
class D:
    def __init__(self,name):
        self.name=name
    def __get__(self,instance,owner):
        print('get')
        return instance.__dict__.get(self.name)
    def __set__(self,instance,value):
        print('set')
        instance.__dict__[self.name]=value
class C:
    x=D('x')
c=C()
c.x
print(c.__dict__)
c.x=250
print(c.__dict__)
print(c.x)

```

改进：

```
class D:
    def __set_name__(self,owner,name):
        self.name=name
    def __get__(self,instance,owner):
        print('get')
        return instance.__dict__.get(self.name)
    def __set__(self,instance,value):
        print('set')
        instance.__dict__[self.name]=value
class C:
    x=D()
c=C()
c.x
print(c.__dict__)
c.x=250
print(c.__dict__)
print(c.x)
```



![QQ_1739685757510](pytohn学习.assets/QQ_1739685757510.png)

## 75.类和对象（19）函数方法静态方法类方法的底层实现原理

函数是一个非数据描述符

```
class C:
    def func(self,x):
        return x
c=C()
C.func#函数
c.fun#方法
```

调用方式访问,串联装饰器

```
class C:
    @classmethod
    def __doc__(cls):
        return f'I love fishc from class {cls.__name__}'
c=C()
print(c.__doc__())
print(C.__doc__())
```

```
class D:
    @classmethod
    @property
    def __doc__(cls):
        return  f'i love fishc from class {cls.__name__}'
d=D()
d.__doc__
D.__doc__
```

多个装饰器串联自下往上

hasattr原理：

```
class methodtype:
    def __init__(self,func,obj):
        self.__func__=func
        self.__self__=obj
    def __call__(self,*args,**kwargs):
        func=self.__func__
        obj=self.__self__
        print('小白')
        return func(obj,*args,**kwargs)
class Classnethond:
    def __init__(self,f):
        self.f=f
    def __get__(self,obj,cls=None):
        if cls is None:
            print('旺财')
            cls=type(obj)
        if hasattr(type(self.f),'__get__'):
            print(f'来福，type(self.f)->{type(self.f)}')
            return self.f.__get__(cls,cls)
        return methodtype(self.f,cls)
class D:
    @Classnethond
    @property
    def __doc__(cls):
        return f'i love fishc from class {cls.__name__}'
d=D()
d.__doc__
```

![QQ_1739700441798](pytohn学习.assets/QQ_1739700441798.png)

不加@property也是打印这个

## 76.类和对象（20）类装饰器

在类被实例化之前对其进行拦截和干预

```python
def report(cls):
    def oncall(*args,**kwargs):#args=(1,2,3)
        print('我要开始实例化对象了')
        _=cls(*args,**kwargs)#解包
        print('实例化已经完成')
        return _
    return oncall
@report#C=report(C)
class C:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print('构造函数被调用了')
c=C(1,2,3)#oncall(1,2,3)
```

让类来做装饰器，用它装饰函数

引入：

```
class counter:
    def __init__(self):
        self.count=0
    def __call__(self,*args,**kwargs):
        self.count+=1
        print(f'已经被调用了{self.count}次')
c=counter()
c()
c()
c()
```

![QQ_1739703084690](pytohn学习.assets/QQ_1739703084690.png)

```
class counter:
    def __init__(self,func):
        self.count=0
        self.func=func
        
    def __call__(self,*args,**kwargs):
        self.count+=1
        print(f'已经被调用了{self.count}次')
        return self.func(*args,**kwargs)
@counter#sayhi=counter(sayhi),sayji已经变成counter的一个实例化对象

def sayhi():
    print('hi')
sayhi()#对象当成函数用，会调用call
sayhi()
sayhi()

```

```
class check:
    def __init__(self, cls):
        self.cls=cls
    def __call__(self,*args,**kwargs):
        self.obj=self.cls(*args,**kwargs)
        return self
    def __getattr__(self,name):
        print('正在访问{self.name}')
        return getattr(self.obj,name)
@check#C=check(C)
class C:
    def sayhi(self):
        print('hi')
    def sayhey(self):
        print('hey')
c=C()
c.sayhi()
c.sayhey()
```

下面来看一个bug

```
class check:
    def __init__(self, cls):
        self.cls=cls
    def __call__(self,*args,**kwargs):
        self.obj=self.cls(*args,**kwargs)
        return self
    def __getattr__(self,name):
        print(f'正在访问{name}')
        return getattr(self.obj,name)
@check#C=check(C)，产生对象,实例化一次
class C:
    def __init__(self,name):
        self.name=name
    def sayhi(self):
        print(f'hi {self.name}')
    def sayhey(self):
        print(f'hey {self.name}')

c1=C('c1')#c1,c2均是check类对象，c1c2访问2次call
c2=C('c2')#self.obj,c1被c2覆盖
c1.name
c2.name
c1.sayhi()
c2.sayhey()

```

![QQ_1739706321772](pytohn学习.assets/QQ_1739706321772.png)



改进：外面加一层函数



```python
def report(cls):
    class check:
        def __init__(self, *args,**kwargs):
             self.obj=cls(*args,**kwargs)

        def __getattr__(self,name):
            print(f'正在访问{name}')
            return getattr(self.obj,name)
    return check
@report#C=report(C)
class C:#被替换为class check
    def __init__(self,name):
        self.name=name
    def sayhi(self):
        print(f'hi {self.name}')
    def sayhey(self):
        print(f'hey {self.name}')

c1=C('c1')#实例化2次
c2=C('c2')
c1.name
c2.name
c1.sayhi()
c2.sayhey()
```

![QQ_1739707324890](pytohn学习.assets/QQ_1739707324890.png)

## 77.类和对象（21）type()

```
print(int)
type('lainua') is str#返回对象对应的类，True
type([])('lainhua')
type({}).fromkeys('python')

class C:
    def __init__(self,x):
        self.x=x
c=C(520)
d=type(c)(520)
print(c.__class__)
print(d.__class__)
type(C)#type,类也是type生成的对象
type(type)#type
```

```
class C:
    pass
C=type('C',(),{})#名字，父类默认object,函数和属性
c=C()
c.__class__
C.__bases__
D=type('D',(C,),{})
D.__bases__
E=type('E',(),dict(x=250,y=520))
E.x
E.y

```

```
def func(self,name='lainhua'):#因为是类，所以要self
    print(f'hello {name}')
F=type('F',(),dict(sayhi=func))
f=F()
f.sayhi()
f.sayhi('py')
```

```
#__init_subclass__()
class C:
    def __init_subclass__(cls):
        print('父爱如山')
        cls.x=520
class D(C):
    x=250
print(D.x)
```

![QQ_1739612215991](pytohn学习.assets/QQ_1739612215991.png)

```
class C:
    def __init_subclass__(cls,value):
        print('父爱如山')
        cls.x=value
class D(C,value=520):
    x=250
print(D.x)

```

```
class C:
    def __init_subclass__(cls,value1,value2):
        print('父爱如山')
        cls.x=value1
        cls.y=value2
D=type('D',(C,),dict(x=250),value1=520,value2=666)
print(D.x)
print(D.y)
```

## 78.类和对象（22）元类

类，元类，type

```
class Metac(type):
    pass
class C(metaclass=Metac):
    pass
c=C()
print(type(c))
print(type(C))
print(type(Metac))
```

![QQ_1739617501330](pytohn学习.assets/QQ_1739617501330.png)

```
class metac(type):
    def __new__(mcls,name,bases,attrs):
        print('new in metac')
        return type.__new__(mcls,name,bases,attrs)
    def __init__(cls,name,bases,attrs):
        print('init in metac')
        type.__init__(cls,name,bases,attrs)
class C(metaclass=metac):
    def __new__(cls):
        print('new in C')
        return super().__new__(cls)#object
    def __init__(self):
        print('init in C')
c=C()
```



```python
class metac(type):
    def __new__(mcls,name,bases,attrs):
        print('new in metac')
        print(f'mcls={mcls},name={name},bases={bases},sttrs={attrs}')
        return type.__new__(mcls,name,bases,attrs)
    def __init__(cls,name,bases,attrs):
        print('init in metac')
        print(f'cls={cls},name={name},bases={bases},sttrs={attrs}')

        type.__init__(cls,name,bases,attrs)
class C(metaclass=metac):
    def __new__(cls):
        print('new in C')
        return super().__new__(cls)#object
    def __init__(self):
        print('init in C')
c=C()
```

call方法：类：拦截对象被当作函数调用的时候的操作

元类：拦截类实例化对象的操作

```python
class metac(type):
    def __call__(cls,*args,**kwargs):
        print('call in metac')
class C(metaclass=metac):
    pass
c=C()  
```

![QQ_1739619899614](pytohn学习.assets/QQ_1739619899614.png)

![QQ_1739620155674](pytohn学习.assets/QQ_1739620155674.png)

## 79.类和对象（23）元类的应用

### 1.给所有的类都添加一个属性

```python
class metac(type):
    def __new__(mcls,name,bases,attrs):
        attrs['author']='lianhua'
        return type.__new__(mcls,name,bases,attrs)
class C(metaclass=metac):
    pass
class D(metaclass=metac):
    pass
c=C()
d=D()
print(c.author)
print(c.author)
```

![QQ_1739620995070](pytohn学习.assets/QQ_1739620995070.png)

同样的：



```python
class metac(type):
    def __init__(cls,name,bases,attrs):
        cls.author='lianhua'
        return type.__init__(cls,name,bases,attrs)
class C(metaclass=metac):
    pass
class D(metaclass=metac):
    pass
c=C()
d=D()
print(c.author)
print(c.author)
```

### 2.对类名的定义规范做限制

![QQ_1739621355706](pytohn学习.assets/QQ_1739621355706.png)

### 3.修改对象的属性值

call

```python
class metac(type):
    def __call__(cls,*args,**kwargs):
        new_args=[each.upper() for  each in args if isinstance(each,str)]
        return type.__call__(cls,*new_args,**kwargs)
class C(metaclass=metac):
    def __init__(self,name):
        self.name=name
c=C('LianHua')
print(c.name)
```



### 4.限制类实例化时的传参方式

```
class metac(type):
    def __call__(cls,*args,**kwargs):
        if args:
            raise TypeError('仅支持关键字对象')
        return type.__call__(cls,*args,**kwargs)
class C(metaclass=metac):
    def __init__(self,name):
        self.name=name
c=C('name=lianhua')
print(c.name)
```

### 5.禁止一个类被实例化

```
class noinstance(type):
    def __call__(self, *args, **kwds):
        raise TypeError('该类不支持实例化')
class C(metaclass=noinstance):
    pass
```

改进：

```
class noinstance(type):
    def __call__(self, *args, **kwds):
        raise TypeError('该类不支持实例化')
class C(metaclass=noinstance):
    @staticmethod
    def ok():
        print('静态直接访问是被允许的')
    @classmethod
    def ok1(cls):
        print('类方法直接访问是被允许的')
C.ok()
C.ok1()
```

![QQ_1739631332898](pytohn学习.assets/QQ_1739631332898.png)

### 6.只允许实例化一个对象

```
class noinstance(type):
    def __init__(cls, *args, **kwargs):
        cls.__a=None
        type.__init__(cls,*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__a is None:
            cls.__a=type.__call__(cls,*args,**kwargs)
            return cls.__a
        else:
            return cls.__a
class C(metaclass=noinstance):
    pass

c1=C()
c2=C()
print(c1 is c2)
```

![QQ_1739631864231](pytohn学习.assets/QQ_1739631864231.png)

## 80.类和对象（24）抽象基类

1.不能被直接实例化，只能被继承使用

2.子类必须实现抽象基类中实现的抽象方法，否则无法实例化

3.是一个鸭子类型的一个补充

![QQ_1739632759670](pytohn学习.assets/QQ_1739632759670.png)

![QQ_1739633080760](pytohn学习.assets/QQ_1739633080760.png)

正确代码：

```
from abc import ABCMeta,abstractmethod
class fruit(metaclass=ABCMeta):#抽象基类这样写就行了
    def __init__(self,name):
        self.name=name
    @abstractmethod#抽象方法
    def good(self):
        pass
class banana(fruit):
    def good(self):
        print('多吃香蕉身体好')
    pass
b=banana('香蕉')
b.good()

```

抽象基类让bug提前暴露

是编程规范的手段

![QQ_1739635618614](pytohn学习.assets/QQ_1739635618614.png)

```python
from abc import ABCMeta,abstractmethod
class animal(metaclass=ABCMeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def intro(self):
        pass
    @abstractmethod
    def say(self):
        pass

class cat(animal):
    def intro(self):
        print(f'我是一只猫，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('mua')

class dog(animal):
    def intro(self):
        print(f'我是一只狗，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('wow')

class pig(animal):
    def intro(self):
        print(f'我是一只猪，我叫{self.name},今年{self.age}岁')
    def say(self):
        print('en')
c=cat('web',14)
d=dog('lian',12)
c=pig('hua',11)
c.say()
```



## 81.类和对象（25）

总结聊天

## 82.模块和包（上）

代码打包：函数，类和方法，模块（最高级）

![QQ_1739636512714](pytohn学习.assets/QQ_1739636512714.png)



```
import hello
hello.sayhi()
hello.sayhello()
```

1. **基本导入：`import module`**

   - 导入整个模块，使用时需通过模块名前缀访问内部对象。
   ```python
   import math
   print(math.sqrt(16))  # 输出: 4.0
   ```

---

### 2. **导入特定对象：`from module import obj1, obj2`**

   - 直接导入模块中的特定函数、类或变量，无需模块名前缀。
   ```python
   from math import sqrt, pi
   print(sqrt(25))  # 输出: 5.0
   print(pi)        # 输出: 3.141592653589793
   ```

---

### 3. **导入全部对象：`from module import *`**（不推荐）

   - 导入模块中的所有对象（不以下划线 `_` 开头的对象），可能导致命名冲突。
   ```python
   from math import *
   print(sin(0))    # 输出: 0.0
   print(log10(100))  # 输出: 2.0
   ```

---

### 4. **别名导入：`import module as alias`**

   - 为模块或对象设置别名，简化代码或避免命名冲突。
   ```python
   import numpy as np
   from datetime import datetime as dt

   arr = np.array([1, 2, 3])
   now = dt.now()
   ```

---

### 5. **导入子模块：`import package.submodule`**

   - 当模块位于包（Package）中时，通过路径导入子模块。
   ```python
   import urllib.request
   response = urllib.request.urlopen("https://www.example.com")
   ```

---

### 6. **相对导入（在包内部使用）**

   - 在包的内部模块中，使用 `.` 表示当前目录，`..` 表示上级目录。
   ```python
   # 文件结构：
   # mypackage/
   #   __init__.py
   #   module1.py
   #   subpackage/
   #     __init__.py
   #     module2.py

   # 在 module2.py 中导入同级的 module1.py
   from .. import module1
   ```

---

### 7. **动态导入：`importlib`**

   - 运行时根据条件动态导入模块。
   ```python
   import importlib

   module_name = "math"
   math_module = importlib.import_module(module_name)
   print(math_module.sqrt(9))  # 输出: 3.0
   ```

---

### 8. **`sys.path` 和自定义路径**

   - 添加自定义路径到 Python 的模块搜索路径（`sys.path`）。
   ```python
   import sys
   sys.path.append("/path/to/your/module")
   import my_custom_module
   ```

---

### **注意事项**

1. **避免循环导入**：模块 A 导入模块 B，同时模块 B 又导入模块 A。
2. **模块缓存**：Python 会缓存已导入的模块（`sys.modules`），重复导入不会重新加载。
3. **`__init__.py`**：在包目录中，此文件标识该目录为 Python 包（Python 3.3+ 可选，但建议保留）。
4. **`if __name__ == "__main__"`**：用于区分模块是被导入还是直接运行。

---

### **总结**

| 方法                 | 适用场景             | 优点         | 缺点             |
| -------------------- | -------------------- | ------------ | ---------------- |
| `import module`      | 需要模块内多个对象时 | 避免命名冲突 | 代码冗余         |
| `from module import` | 仅需少量对象时       | 简化代码     | 可能引发命名冲突 |
| 别名导入             | 模块名较长或冲突时   | 提高可读性   | 需要额外记忆别名 |
| 相对导入             | 包内部模块间的引用   | 路径清晰     | 仅限包内使用     |

![QQ_1739636767699](pytohn学习.assets/QQ_1739636767699.png)

![QQ_1739636892770](pytohn学习.assets/QQ_1739636892770.png)

较迟导入的方法将覆盖较早导入的方法

![QQ_1739637117478](pytohn学习.assets/QQ_1739637117478.png)

![QQ_1739637124627](pytohn学习.assets/QQ_1739637124627.png)



![QQ_1739637263836](pytohn学习.assets/QQ_1739637263836.png)

## 83.模块和包（中）

### 1.模块

模块导入过程中会从头到尾执行所有语句

```
import transfer1
print(f'32摄氏度={transfer1.c2f(32):.2f}华氏度')
print(f'99摄氏度={transfer1.c2f(99):.2f}华氏度')

```

```
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
```

![QQ_1739638444286](pytohn学习.assets/QQ_1739638444286.png)

### 2.包

```
import TC.pp
print(f'32摄氏度={TC.pp.c2f(32):.2f}华氏度')
print(f'99摄氏度={TC.pp.c2f(99):.2f}华氏度')

```

![QQ_1739641287262](pytohn学习.assets/QQ_1739641287262.png)

可以编写init对包初始化

![QQ_1739641553904](pytohn学习.assets/QQ_1739641553904.png)

```
import TC.pp

print(f'32摄氏度={TC.pp.c2f(32):.2f}华氏度')
print(f'99摄氏度={TC.pp.c2f(99):.2f}华氏度')

```

![QQ_1739641577684](pytohn学习.assets/QQ_1739641577684.png)

全局变量跨文件修改

![QQ_1739642075290](pytohn学习.assets/QQ_1739642075290.png)

![QQ_1739642083366](pytohn学习.assets/QQ_1739642083366.png)

![QQ_1739642089611](pytohn学习.assets/QQ_1739642089611.png)

![QQ_1739642098553](pytohn学习.assets/QQ_1739642098553.png)

### 3.解决太多包

1.as 

2.init

![QQ_1739642260353](pytohn学习.assets/QQ_1739642260353.png)

![QQ_1739642267858](pytohn学习.assets/QQ_1739642267858.png)

### 4.遏制from import*的伤害

#### 1.在模块中：

```
__all__['sayhi','x']
```

#### 2.在包中：

在构造文件init中

```
__all__=['fc1','fc2']
```

```
from TC import *
print(dir())
fc1.sayhi()
fc2.sayhello()
```

## 84.模块和包（下）

将代码部署到 PyPI（Python Package Index）需要遵循特定的框架和流程。以下是详细的步骤和工具说明：

---

### **1. 准备工作**
#### 1.1 项目结构
确保你的项目具有标准的目录结构，例如：
```
my_package/
├── my_package/          # 主代码目录
│   ├── __init__.py
│   └── module.py
├── tests/               # 单元测试
├── README.md            # 项目说明
├── LICENSE              # 许可证
└── pyproject.toml       # 构建配置（现代方式）
# 或 setup.py + setup.cfg（传统方式）
```

#### 1.2 注册 PyPI 账号
- 前往 [PyPI](https://pypi.org/) 和 [TestPyPI](https://test.pypi.org/) 注册账号。
- 生成 API Token（推荐替代密码）：在账号设置中创建 Token，权限选择整个账户或指定项目。

---

### **2. 选择构建工具**
#### 2.1 传统方式：`setuptools` + `twine`
1. **创建 `setup.py` 或 `setup.cfg`**（旧版）：
   ```python
   # setup.py
   from setuptools import setup, find_packages
   
   setup(
       name="my_package",
       version="0.1.0",
       author="Your Name",
       description="A short description",
       long_description=open("README.md").read(),
       long_description_content_type="text/markdown",
       packages=find_packages(),
       install_requires=["requests>=2.25.1"],  # 依赖
       classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
       ],
       python_requires=">=3.6",
   )
   ```

2. **创建 `pyproject.toml`**（现代方式，推荐）：
   ```toml
   [build-system]
   requires = ["setuptools>=61.0", "wheel"]
   build-backend = "setuptools.build_meta"
   ```

#### 2.2 现代方式：`poetry` 或 `flit`
- **Poetry**（推荐）：
  ```bash
  # 安装
  pip install poetry
  
  # 初始化配置（生成 pyproject.toml）
  poetry init
  
  # 添加依赖
  poetry add requests
  ```

- **Flit**：
  ```bash
  pip install flit
  flit init  # 生成 pyproject.toml
  ```

---

### **3. 生成分发包**
#### 3.1 构建源码包和 wheel
```bash
# 使用 setuptools
python -m build

# 或使用 poetry
poetry build
```

生成的包在 `dist/` 目录下：
- `my_package-0.1.0.tar.gz`（源码包）
- `my_package-0.1.0-py3-none-any.whl`（wheel 包）

---

### **4. 上传到 PyPI**
#### 4.1 使用 `twine`（推荐）
```bash
# 安装 twine
pip install twine

# 上传到 TestPyPI（测试用）
twine upload --repository testpypi dist/*

# 上传到正式 PyPI
twine upload dist/*
```

#### 4.2 配置 API Token
- 在 `~/.pypirc` 中配置 Token（可选）：
  ```ini
  [pypi]
  username = __token__
  password = pypi-<你的API Token>
  ```

---

### **5. 验证安装**
```bash
# 从 PyPI 安装测试
pip install my_package

# 或从 TestPyPI 安装
pip install -i https://test.pypi.org/simple/ my_package
```

---

### **6. 版本更新**
1. 修改版本号（在 `pyproject.toml`、`setup.py` 或 `__version__.py` 中）。
2. 重新构建并上传：
   ```bash
   python -m build
   twine upload dist/*
   ```

---

### **关键工具总结**
| 工具         | 用途                         |
| ------------ | ---------------------------- |
| `setuptools` | 构建分发包（源码和 wheel）   |
| `twine`      | 安全上传包到 PyPI            |
| `poetry`     | 依赖管理 + 构建 + 发布一体化 |
| `wheel`      | 生成二进制 wheel 包          |

---

### **常见问题**

1. **版本冲突**：每次上传必须更新版本号。
2. **TestPyPI 测试**：避免在正式环境出错。
3. **依赖声明**：务必在 `install_requires` 或 `pyproject.toml` 中明确依赖。

通过以上步骤，你可以将代码规范地部署到 PyPI，供其他用户安装使用。
