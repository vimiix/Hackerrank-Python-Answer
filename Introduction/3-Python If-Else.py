if __name__ == '__main__':
    n = int(raw_input())
    if n % 2:
        out = 'Weird'
    elif n in range(2,6):
        out = 'Not Weird'
    elif n in range(6,21):
        out = 'Weird'
    else:
        out = 'Not Weird'   
    print out