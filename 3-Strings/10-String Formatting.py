from __future__ import print_function
def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in xrange(1, number+1):
        print (str(i).rjust(width), oct(i)[1:].rjust(width), hex(i)[2:].upper().rjust(width),bin(i)[2:].rjust(width), sep=' ')


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
