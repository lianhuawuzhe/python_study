# f=open('FishC.txt','w')
# f.write('I love FishC.')
# 1/0#打断语句，未写入硬盘
# f.close()


# with open('FishC.txt.','w') as f:
#     f.write('I love FishC')
#     1/0#同样报错，但是with会帮我关闭
# import pickle

# x,y,z=1,2,3
# s='lianhua'
# l=['莲华',520,3.14]
# d={'one':1,'two':2}

# with open('data.pk1','wb') as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)
#     pickle.dump(z,f)
#     pickle.dump(s,f)
#     pickle.dump(l,f)
#     pickle.dump(d,f)

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


#改进
import pickle
with open('data.pk1','rb') as f:
    x,y,z,s,l,d=pickle.load(f)#解包

print(x,y,z,s,l,d,sep='\n')

