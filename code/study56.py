# try:
#     1/0
# except:
#     print('逮到了')
# else:
#     print('没逮到')
# finally:
#     print('逮没逮到都会执行')


# try:
#     f=open('fishc.txt','w')
# except:
#     print('出错了')
# finally:
#     f.close()
 

# try:
#     while True:
#         pass
# finally:
#     print('晚安')

# try:
#     try:
#         520+'lianhua'
#     except:
#         print('内部异常')
#     1/0
# except:
#     print('外部异常')
# finally:
#     print('收尾工作')

# raise ValueError('值不正确')
# #不能用raise生成不存在的异常
# try:
#     1/0
# except:
#     raise ValueError('这样不行')#偷天换日

# #异常链
# raise ValueError('这样可不行') from ZeroDivisionError

# s='fishc'
# assert s=='fishc'
# assert!='fishc'

# try:
#     while True:
#         while True:
#             for i in range(10):
#                 if i>3:
#                     raise
#                 print(i)
#             print('被跳过')
#         print('被跳过')
#     print('被跳过')
# except:
#     print('到这儿来了')
        