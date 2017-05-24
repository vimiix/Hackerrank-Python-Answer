def swap_case(s):
    list = []
    for i in range(len(s)):
        if s[i].islower():
            list.append(s[i].upper())
        else:
            list.append(s[i].lower())
    return ''.join(list)


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
