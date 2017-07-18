# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
SubE = raw_input().split(' ')
b = raw_input()
SubF = raw_input().split(' ')

Total_list = set(SubE).intersection(SubF)
print len(Total_list)
