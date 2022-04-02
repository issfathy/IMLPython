
from IMLMachine import IMLMachine

def main():
    inFile = None
    print("Please enter the file name of the program to load:")
    kb = input()
    fileName = open(kb)
    try:
        inFile = fileName.read()
        fileName.close()

    except: 
        print("Illegal file.")
        exit()
    
    
    machine = IMLMachine.IMLmachine(inFile)
    print(machine)
    IMLMachine.run()
    print(machine)


main()
