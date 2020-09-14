import sys

if __name__== "__main__": #if arg provided then serve as name
    try:
        name = sys.argv[1]
    except:
        name = input("What's your name?\n")
    from getpass import getpass
    pw = getpass("What's your password?\n")
    print(name, pw)
