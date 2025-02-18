# from pathlib import Path#这种导入后面不加入模块名
# p=Path.cwd()#获取文件当前目录
# print(p)
# #路径拼接
# q=p/'lianhua.txt'
# p.is_dir()
# q.is_dir()
# p.is_file()
# q.is_file()
# p.exists()
# q.exists()
# Path('C/404').exists()
# p.name
# q.name
# q.stem
# p.parent
# q.suffix
# ps=p.parents
# for each in ps:
#     print(each)
# ps[0]#剪掉一节
# ps[1]
# p.parts
# p.stat().st_size
# p.stat()


# Path('./doc')#相对路径，当前路径下doc这个文件夹
# Path('../lianhua')#上一级路径
# Path('./doc').resolve()#相对变绝对
# p.iterdir()#获取当前路径下所有的子文件和子文件夹,得到一个生成器
# for each in p.iterdir():
#     print(each)
# [x for x in p.iterdir() if x.is_file]

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


