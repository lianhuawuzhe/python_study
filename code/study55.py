# 'lianhua'+520

# try:
#     1/0
# except ZeroDivisionError as e:#精确定位
#     print(e)

# try:
#     1/0
#     520+'lianhua'
# except (ZeroDivisionError,ValueError,TypeError):
#     pass

try:
    1/0
    520+'lianhua'#会被忽略
except ZeroDivisionError:
    print('除数不能0')
except ValueError:
    print('值不正确')
except TypeError:
    print('类型不正确')
