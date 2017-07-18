# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
country = set()
for i in xrange(n):
    country.add(raw_input())
print(len(country))
