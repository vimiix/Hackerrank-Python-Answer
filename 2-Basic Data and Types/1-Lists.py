if __name__ == '__main__':
    N = int(raw_input())
    index = N
    desList = []
    cmdList = []
    while (N != 0):
        N -= 1
        cmdList.append(raw_input())
    #run each cmd
    for i in range(index):
        cmd = cmdList[i].split(' ')
        if cmd[0] == 'insert':
            desList.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'remove':
            desList.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            desList.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            desList.sort()
        elif cmd[0] == 'pop':
            desList.pop()
        elif cmd[0] == 'reverse':
            desList.reverse()
        elif cmd[0] == 'print':
            print(desList)
        else:
            pass
            
