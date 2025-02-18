# s=[1,2,3,4,5]
# for i in range(len(s)):
#     s[i]*=2
# print(s)
# s=[1,2,3,4,5]
# s=[i*2 for i in s]
# print(s)
# x=[i+1 for i in range(10)]
# print(x)
# x=[]
# for i in range(10):
#     x.append(i+1)
# print(x)
# y=[c*2 for c in 'china']
# print(y)

# code=[ord(c) for c in "china"]
# print(code)
matrix=[[1,2,3]
,[4,5,6]
,[7,8,9]]
col2=[row[1] for row in matrix]
print(col2)
diag=[matrix[i][i] for i in range(len(matrix))]
print(len(matrix))
p=[matrix[i][2-i] for i in range(len(matrix))]
print(p)
print(diag)