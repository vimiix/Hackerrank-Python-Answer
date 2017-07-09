#coding=utf-8

def merge_the_tools(string, k):
    # your code goes here
    arr_list = [string[i:i+k] for i in range(0, len(string), k)]
    for l in arr_list:
        arr = ''.join(x for i,x in enumerate(l) if l.index(x) == i)
        print(arr)


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
