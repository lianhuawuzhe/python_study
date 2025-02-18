# s=[1,2,3]
# t=[4,5,6]
# print(s+t)
# print(s*3)
# matrix=[[1,2,3],
# [4,5,6],
# [7,8,9]]
# print(matrix)
# for i in matrix:
#     for each in i:
#         print(each,end='')
#     print()

# print(matrix[0])
# print(matrix[0][1])
A=[0]*3
# print(A)
for i in range(3):
    A[i]=[0]*3
print(A)
# B=[[[0]*3]*3]*3
# print(B)
C=[[0]*3]*3
A[1][1]=1
C[1][1]=1
print(A)
print(C)
x='china'
y='china'
print(x is y)
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(A[0] is A[1])
print(A[1] is A[2])
print(C[0] is C[1])
print(C[1] is C[2])