#coding=utf-8
# Enter your code here. Read input from STDIN. Print output to STDOUT

m,n = raw_input().split()
arr = raw_input().split()
A = set(raw_input().split())
B = set(raw_input().split())

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1      
print(happiness)


#下面是网上的大神写的解法，巧妙地运用计算机中True == 1, False == 0，来做数值计算求和。
#print sum([(i in A) - (i in B) for i in arr])
