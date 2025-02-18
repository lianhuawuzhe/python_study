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

def times(s:str='fishc',n:int=3)->str:#类型，默认参数
    return s*n
times('lianhua',5)
times(5,5)

def timed(s:list[int],n:int=3)->list:
    return s*n

def timed(s:dict[str,int],n:int=3)->list:
    return list(s.keys())*n


times.__name__#name获取函数名字
times.__annotations__#以字典类型打印函数里的三个类型注释
exchange.__doc__#查看函数文档