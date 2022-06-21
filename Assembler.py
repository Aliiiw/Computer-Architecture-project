from atexit import register


commandsOpCodes = {

    "add" : "000000",
    "sub" : "000000",
    "addi": "001000",
    "lw"  : "100011",
    "sw"  : "101011",
    "lh"  : "100001",
    "lhu" : "100101",
    "sh"  : "101001",
    "lb"  : "100000",
    "lbu" : "100100",
    "sb"  : "101000",
    "and" : "000000",
    "or"  : "000000",
    "nor" : "000000",
    "andi": "001100",
    "ori" : "001101",
    "sll" : "000000",
    "srl" : "000000",
    "beq" : "000100",
    "bne" : "000101",
    "slt" : "000000",
    "sltu": "000000",
    "slti": "001010",
    "j"   : "000010",
    "jr"  : "000000",
    "jal" : "000011",
  
}

registersValue = {
    "zero": "000000",
    "at" : "00001" ,
    "v0" : "00010",
    "v1" : "00011",
    "a0" : "00100",
    "a1" : "00101",
    "a2" : "00110",
    "a3" : "00111",
    "t0" : "01000",
    "t1" : "01001",
    "t2" : "01010",
    "t3" : "01011",
    "t4" : "01100",
    "t5" : "01101",
    "t6" : "01110",
    "t7" : "01111",
    "s0" : "10000",
    "s1" : "10001",
    "s2" : "10010",
    "s3" : "10011",
    "s4" : "10100",
    "s5" : "10101",
    "s6" : "10110",
    "s7" : "10111",
    "t8" : "11000",
    "t9" : "11001",
    "k0" : "11010",
    "k1" : "11011",
    "gp" : "11100",
    "sp" : "11101",
    "s8" : "11110",
    "ra" : "11111",
}


def assembler(command, operator1, operator2, operator3):
    machineCode = ""
    if command == "add":
        machineCode += commandsOpCodes[command]
        
    elif command == "sub":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "addi":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "lw":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "sw":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "lh":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "lhu":
        machineCode += commandsOpCodes[command]
        pass
    elif command == "sh":
        pass
    elif command == "lb":
        pass
    elif command == "lbu":
        pass
    elif command == "sb":
        pass
    
    elif command == "and":
        pass
    elif command == "or":
        pass
    elif command == "nor":
        pass
    elif command == "andi":
        pass
    elif command == "ori":
        pass
    elif command == "sll":
        pass
    elif command == "srl":
        pass
    elif command == "beq":
        pass
    elif command == "bne":
        pass
    elif command == "slt":
        pass
    elif command == "sltu":
        pass
    elif command == "slti":
        pass
    elif command == "j":
        pass
    elif command == "jr":
        pass
    elif command == "jal":
        pass






    return ""



with open('input.txt') as file:  

    allString = file.read()
    updateString = allString.splitlines()


    for i in range(len(updateString)):                                          
        
        instruction = updateString[i].split(" ")
        
        command = instruction[0].lower()                      
        registers = instruction[1].split(",")                                        

        operator1 = registers[0].lower()                                              
        operator2 = registers[1].lower()
        operator3 = registers[1].lower()

        assembler(command, operator1, operator2, operator3)


        

       



