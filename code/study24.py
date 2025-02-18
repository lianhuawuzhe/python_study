# A=[0]*3
# for i in range(3):
#     A[i]=[0]*3
# print(A)
# A[1][1]=1
# print(A)
# S=[[0]*3 for i in range(3)]
# print(S)
# even=[i+1 for i in range(10) if i%2==0]
# print(even)
# words=['great','fantastic','brilliant','china','fuckyou']
# # p=[words[i] for i in range(5) if words[i][0]=='f']
# fword=[w for w in words if w[0]=='f']
# print(fword)
# print(p)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# flatten=[col for row in matrix for col in row]
# print(flatten)
# flatten=[]
# for row in matrix:
#     for col in row:
#         flatten.append(col)
# print(flatten)
# p=[x+y for x in 'fishc' for y in 'FISHC']
# print(p)
# _=[]
# for x in 'fishc':
#     for y in 'FISHC':
#         _.append(x+y)
# print(_)

p=[[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0]
print(p)
_=[]
for x in range(10):
    if x%2==0:
        for y in range(10):
            if y%3==0:
                _.append([x,y])
print(_)