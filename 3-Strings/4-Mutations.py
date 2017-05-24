def mutate_string(string, position, character):
    #L = list(string)
    #L[position] = character
    #string = "".join(L)
    #return string
    
    #another solution
    string = string[:position] +character+string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
