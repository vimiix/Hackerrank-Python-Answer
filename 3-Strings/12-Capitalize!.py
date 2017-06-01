def capitalize(string):
    for x in string[:].split():
        string = string.replace(x,(x[0].capitalize()+x[1:]))
    return string

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
