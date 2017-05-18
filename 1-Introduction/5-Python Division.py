'''
导入python未来支持的语言特征division(精确除法)，
当我们没有在程序中导入该特征时，"/"操作符执行的是截断除法(Truncating Division),
当我们导入精确除法之后，"/"执行的是精确除法
'''
from __future__ import division 
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    
    print a//b
    print a/b