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