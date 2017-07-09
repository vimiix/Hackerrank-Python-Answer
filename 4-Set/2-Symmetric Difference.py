# Enter your code here. Read input from STDIN. Print output to STDOUT

M = raw_input()
M_set = set(map(int, raw_input().split()))
N = raw_input()
N_set = set(map(int, raw_input().split()))

Symmetric_set = M_set.union(N_set).difference(M_set.intersection(N_set))
arr = list(Symmetric_set)
ordered_arr = sorted(arr)

for i in ordered_arr:
    print i
