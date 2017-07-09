#coding=utf-8

n = input()
s = set(map(int, raw_input().split())) 
N = input()

for _ in xrange(N):
    cmd = raw_input().split()
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
print(sum(s))

#以下是高级解法，适配性更高
'''
#解法1

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
    """
    此处需要标注一下为什么后面需要 +['']
    前面的格式化字符串中最少需要传入两个参数，
    当终端输入remove 8 的时候，format后面的括号内会得到一个列表为：['remove','8','']
    此时格式化只取用了前两个参数，最后的['']就被忽略舍去了；
    当终端输入pop 的时候，会得到一个列表为：['pop','']
    此时将两个参数都传进去，就不会出现缺少参数错误了。
    """
print(sum(s))
'''

'''
#解法2

n = int(input())
s = set(map(int, input().split())) 
t = int(input())

for i in range(t):
    c, *args = map(str,input().split())
    getattr(s,c) (*(int(x) for x in args))
    #次数要熟悉getattr这个自省函数的用法

print (sum(s))
'''
