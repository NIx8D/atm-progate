import os

def cls():
    return os.system('cls' if os.name=='nt' else 'clear')

def alert(txt):
    cls()
    print("=============================================")
    print(txt)
    print("=============================================")