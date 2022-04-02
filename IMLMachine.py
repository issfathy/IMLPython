

ram = [None] * 100
reg = [None] * 5

class IMLMachine():

    def IMLmachine(inFile):
    
        i = 0
        inFile = str(inFile)
        lineArray = inFile.split()
        for line in lineArray:
            line = int(line)
            ram[i] = line
            i = i+1
    
    def run() :
        pc = 0
        done = 0
        while (done == 0):
            print (ram[pc])
            opCode = int(str(ram[pc])[-6:-4])  
            print (opCode)
            param1 = int(str(ram[pc])[-4:-2])
            print(param1)
            param2 = int(str(ram[pc])[-2:])
            print(param2)
            
            if opCode == 00:
                pc = pc + 1

            if opCode == 11: # WRITE                                    
                print(ram[param1])
                break
            elif opCode == 12: # READ                    
                print("Enter data:")
                theInput = int(input())
                ram[param1] = theInput
                print (ram[param1])
                break
            elif opCode == 21: # STORE
                ram[param2] = reg[param1]
                break
            elif opCode == 22: # LOAD
                reg[param1] = ram[param2]
                break
            elif opCode == 31: # ADD
                reg[param1] = (reg[param1] + reg[param2])
                break
            elif opCode == 32: # SUBTRACT
                reg[param1] = (reg[param1]) - (reg[param2])
                break
            elif opCode == 33: # MULTIPLY
                reg[param1] = (reg[param1]) * (reg[param2])
                break
            elif opCode == 34: # DIVIDE
                reg[param1] = (reg[param1]) / (reg[param2])
                break
            elif opCode == 41: # BRANCH
                pc = param1
                break
            elif opCode == 42: # BRANCHZERO
                if ((reg[param2]) == 0):
                    pc = param1
                else:
                    pc = pc+1
                break
            elif opCode == 43: # BRANCHPOS
                if ((reg[param2]) > 0):
                    pc = param1
                else:
                    pc= pc+1
                break                   
            elif opCode == 99: # HALT
                done = 1
                break
        
            if ( (opCode) > 43 or (opCode) < 41): # Increment PC if this wasn't a branch
                pc = pc+1
            if (done):
                break
        